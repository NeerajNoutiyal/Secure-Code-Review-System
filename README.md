# Secure-Code-Review-System
Project Title

Secure Code Review and Vulnerability Detection System

# Abstract

The Secure Code Review System is a cybersecurity project designed to analyze source code and detect common security vulnerabilities in software applications. The system scans program files and identifies insecure coding practices such as SQL Injection, Cross-Site Scripting (XSS), hardcoded passwords, insecure functions, and command injection.

This project helps developers improve software security by automatically reviewing code and generating vulnerability reports.

# Objectives

- Detect security vulnerabilities in source code
- Help developers write secure applications
- Automate basic secure code review
- Generate vulnerability reports
- Improve cybersecurity awareness

# Technologies Used
## Technology    	Purpose
Python         	Backend Programming
Flask         	Web Framework
HTML/CSS	      Frontend
SQLite	        Database
Regex	          Pattern Detection
Bootstrap	      UI Design

# Features
- Upload source code files
- Scan for vulnerabilities
- Detect:
  - SQL Injection
  - XSS
  - Hardcoded Passwords
  - Dangerous Functions
  - Command Injection
- Generate scan reports
- Simple web dashboard
  
<img width="600" height="552" alt="image" src="https://github.com/user-attachments/assets/a6ef8986-38a3-4438-b48e-c880446dc48d" />

# Workflow
1. User uploads source code
2. System scans code
3. Regex-based detection engine analyzes patterns
4. Vulnerabilities identified
5. Report generated


# Project Folder Structure

secure-code-review/
│
├── app.py
├── scanner.py
├── requirements.txt
├── database.db
│
├── templates/
│   ├── index.html
│   └── report.html
│
├── static/
│   └── style.css
│
└── uploads/

