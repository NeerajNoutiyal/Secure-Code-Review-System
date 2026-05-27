import re

patterns = {
    "SQL Injection": r"(SELECT|INSERT|UPDATE|DELETE).*['\"]?\s*\+",
    "Cross Site Scripting (XSS)": r"<script>|innerHTML",
    "Hardcoded Password": r"password\s*=\s*['\"].+['\"]",
    "Command Injection": r"os.system|subprocess.call",
    "Dangerous Function": r"eval\(|exec\("
}

def scan_code(code):
    findings = []

    for vulnerability, pattern in patterns.items():
        matches = re.findall(pattern, code, re.IGNORECASE)

        if matches:
            findings.append({
                "type": vulnerability,
                "count": len(matches)
            })

    return findings
