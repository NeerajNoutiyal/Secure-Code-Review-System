from flask import Flask, render_template, request
import os
from scanner import scan_code

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    file = request.files['file']

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        results = scan_code(code)

        return render_template('report.html', results=results)

    return "No File Uploaded"

if __name__ == '__main__':
    app.run(debug=True)
