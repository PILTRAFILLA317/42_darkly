# 🕵️ 42 Darkly

```ascii
    ██   ██ ██████      ██████   █████  ██████  ██   ██ ██      ██    ██ 
    ██   ██      ██     ██   ██ ██   ██ ██   ██ ██  ██  ██       ██  ██  
    ███████  █████      ██   ██ ███████ ██████  █████   ██        ████   
         ██ ██          ██   ██ ██   ██ ██   ██ ██  ██  ██         ██    
         ██ ███████     ██████  ██   ██ ██   ██ ██   ██ ███████    ██    
```

A comprehensive **web security penetration testing project** that demonstrates common web application vulnerabilities through practical exploitation techniques. This educational platform provides hands-on experience with various attack vectors and security assessment methodologies.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Security Vulnerabilities Catalog](#security-vulnerabilities-catalog)
- [Vulnerability Categories](#vulnerability-categories)
- [Technical Implementation](#technical-implementation)
- [Security Testing Methodology](#security-testing-methodology)
- [Educational Context](#educational-context)
- [Defensive Measures](#defensive-measures)
- [Tools and Techniques](#tools-and-techniques)

---

## 🎯 Overview

**42 Darkly** is an intentionally vulnerable web application designed for educational purposes in the field of cybersecurity. The project serves as a comprehensive training platform for learning about web application security, penetration testing techniques, and vulnerability assessment methodologies.

This implementation demonstrates:
- **Common Web Vulnerabilities** from the OWASP Top 10
- **Practical Exploitation Techniques** with real-world attack scenarios
- **Security Assessment Methodologies** for vulnerability discovery
- **Manual and Automated Testing** approaches for security evaluation
- **Educational Framework** for cybersecurity skill development

### Project Purpose
- **Educational Training**: Hands-on learning environment for security professionals
- **Vulnerability Research**: Understanding attack vectors and exploitation methods
- **Security Awareness**: Demonstrating real-world security risks in web applications
- **Skill Development**: Practical experience with penetration testing tools and techniques

---

## 🔍 Security Vulnerabilities Catalog

### Authentication & Authorization Flaws

| Vulnerability | Category | Difficulty | Description |
|--------------|----------|------------|-------------|
| [**Cookie Admin True**](/cookie_admin_true/Ressources/README.md) | Access Control | ⭐⭐ | Privilege escalation through cookie manipulation |
| [**Login Brute Force**](/login_brute_force/Ressources/README.md) | Authentication | ⭐⭐⭐ | Credential enumeration using automated attacks |
| [**htpasswd**](/htpasswd/Ressources/README.md) | Authentication | ⭐⭐ | HTTP basic authentication bypass techniques |

### Injection Vulnerabilities

| Vulnerability | Category | Difficulty | Description |
|--------------|----------|------------|-------------|
| [**Search Image Form Injection**](/search_image_form_injection/Ressources/README.md) | SQL Injection | ⭐⭐⭐⭐ | Database manipulation through Union-based SQL injection |
| [**Search Member Form Injection**](/search_member_form_injection/Ressources/README.md) | SQL Injection | ⭐⭐⭐⭐ | Information disclosure via database enumeration |
| [**XSS Feedback**](/xss_feedback/Ressources/README.md) | Cross-Site Scripting | ⭐⭐⭐ | Client-side code injection through feedback forms |
| [**XSS Src Query**](/xss_src_query/Ressources/README.md) | Cross-Site Scripting | ⭐⭐⭐ | Reflected XSS through URL parameters |

### File System & Path Vulnerabilities

| Vulnerability | Category | Difficulty | Description |
|--------------|----------|------------|-------------|
| [**Path Traversal**](/path_traversal/Ressources/README.md) | Directory Traversal | ⭐⭐⭐ | Server file system access through path manipulation |
| [**Upload Image PHP**](/upload_image_php/Ressources/README.md) | File Upload | ⭐⭐⭐⭐ | Malicious file upload and execution |
| [**Hidden Routes**](/hidden_routes/Ressources/README.md) | Information Disclosure | ⭐⭐ | Discovery of unauthorized application endpoints |

### Web Application Logic Flaws

| Vulnerability | Category | Difficulty | Description |
|--------------|----------|------------|-------------|
| [**Http Header Referer**](/http_header_referer/Ressources/README.md) | Header Manipulation | ⭐⭐ | HTTP header-based access control bypass |
| [**Recover Password Form Input**](/recover_password_form_input/Ressources/README.md) | Input Validation | ⭐⭐⭐ | Password recovery mechanism exploitation |
| [**Redirect Page**](/redirect_page/Ressources/README.md) | Open Redirect | ⭐⭐ | Unvalidated redirect and forward attacks |
| [**Survey Form Select**](/survey_form_select/Ressources/README.md) | Input Manipulation | ⭐⭐ | Form validation bypass techniques |

---

## 🛡️ Vulnerability Categories

### 1. **Injection Attacks**
**Description**: Flaws that allow untrusted data to be sent to an interpreter as part of a command or query.

**Examples in Project**:
- **SQL Injection**: Database queries manipulation through form inputs
- **Cross-Site Scripting (XSS)**: JavaScript code injection in web pages
- **Command Injection**: Operating system command execution

**Impact**: Data theft, system compromise, privilege escalation

### 2. **Broken Authentication**
**Description**: Application functions related to authentication and session management implemented incorrectly.

**Examples in Project**:
- **Brute Force Attacks**: Automated credential guessing
- **Session Management**: Cookie manipulation and session hijacking
- **Password Recovery**: Weak password reset mechanisms

**Impact**: Account takeover, identity theft, unauthorized access

### 3. **Security Misconfiguration**
**Description**: Insecure default configurations, incomplete setups, or misconfigured security headers.

**Examples in Project**:
- **Directory Listing**: Exposed directory structures
- **Default Credentials**: Unchanged default passwords
- **Information Disclosure**: Sensitive data exposure

**Impact**: System compromise, data exposure, privilege escalation

### 4. **Insecure Direct Object References**
**Description**: Direct access to objects based on user input without proper authorization checks.

**Examples in Project**:
- **Path Traversal**: File system access through URL manipulation
- **Parameter Tampering**: Unauthorized data access through ID modification

**Impact**: Unauthorized data access, system file exposure

---

## ⚙️ Technical Implementation

### Project Structure
```
42_darkly/
├── cookie_admin_true/          # Cookie manipulation exploit
├── hidden_routes/              # Directory enumeration and hidden paths
├── htpasswd/                   # HTTP authentication bypass
├── http_header_referer/        # HTTP header manipulation
├── login_brute_force/          # Automated credential attacks
│   ├── bruteLogin.py          # Python brute force script
│   └── data.py                # Username and password wordlists
├── path_traversal/             # Directory traversal attack
├── recover_password_form_input/ # Password recovery exploitation
├── redirect_page/              # Open redirect vulnerability
├── search_image_form_injection/ # SQL injection in image search
├── search_member_form_injection/ # SQL injection in member search
├── survey_form_select/         # Form validation bypass
├── upload_image_php/           # Malicious file upload
├── xss_feedback/               # XSS in feedback form
└── xss_src_query/              # Reflected XSS through URL parameters
```

### Attack Methodologies

#### 1. **SQL Injection Techniques**
```sql
-- Database enumeration
1 UNION SELECT database(), NULL --

-- Table discovery  
1 UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema = database() --

-- Column enumeration
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'target_table' --

-- Data extraction
1 UNION SELECT username, password FROM users --
```

#### 2. **Brute Force Implementation**
```python
def bruteForce(thread, cores):
    for user in usernames:
        for password in passwords:
            res = requests.get(
                url=URL,
                params={
                    "page": "signin",
                    "username": user,
                    "password": password
                }
            )
            if "images/WrongAnswer.gif" not in res.text:
                print(f"[SUCCESS] {user}:{password}")
```

#### 3. **Path Traversal Exploitation**
```
# Basic path traversal
/?page=../../../etc/passwd

# Nested directory traversal
/?page=../../../../../../../etc/passwd

# Encoded path traversal
/?page=..%2f..%2f..%2fetc%2fpasswd
```

---

## 🔬 Security Testing Methodology

### 1. **Reconnaissance Phase**
- **Application Mapping**: Identify all accessible endpoints and functionalities
- **Technology Stack**: Determine web server, database, and programming language
- **Entry Points**: Locate forms, parameters, and user input mechanisms

### 2. **Vulnerability Discovery**
- **Automated Scanning**: Use tools like Burp Suite, OWASP ZAP, or Nikto
- **Manual Testing**: Systematic testing of input validation and business logic
- **Code Review**: Static analysis of client-side code and exposed information

### 3. **Exploitation Phase**
- **Proof of Concept**: Develop working exploits for identified vulnerabilities
- **Impact Assessment**: Determine the scope and severity of each vulnerability
- **Documentation**: Record attack vectors, payloads, and exploitation steps

### 4. **Post-Exploitation Analysis**
- **Privilege Escalation**: Attempt to gain higher-level system access
- **Data Extraction**: Identify and retrieve sensitive information
- **Persistence**: Explore methods for maintaining access

---

## 🎓 Educational Context

This project is designed for **cybersecurity education** and provides practical experience with:

### Core Learning Objectives
- **Vulnerability Assessment**: Understanding common web application security flaws
- **Penetration Testing**: Hands-on experience with ethical hacking techniques
- **Security Awareness**: Recognizing and mitigating security risks
- **Tool Proficiency**: Using industry-standard security testing tools

### Skills Developed
- **Manual Testing Techniques**: Identifying vulnerabilities through systematic testing
- **Automated Tool Usage**: Leveraging security scanners and custom scripts
- **Exploitation Development**: Creating proof-of-concept attacks
- **Security Documentation**: Reporting and communicating security findings

### Real-World Applications
- **Web Application Security**: Understanding common attack vectors in web development
- **Security Consulting**: Practical skills for security assessment services
- **Incident Response**: Recognizing attack patterns and indicators of compromise
- **Secure Development**: Building security-conscious development practices

---

## 🛡️ Defensive Measures

### Input Validation and Sanitization
```php
// Proper input validation
function sanitizeInput($input) {
    $input = trim($input);
    $input = stripslashes($input);
    $input = htmlspecialchars($input);
    return $input;
}

// Parameterized queries
$stmt = $pdo->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
$stmt->execute([$username, $password]);
```

### Authentication Security
```php
// Secure session management
session_start();
session_regenerate_id(true);

// Strong password hashing
$hashedPassword = password_hash($password, PASSWORD_ARGON2ID);

// Account lockout mechanism
if ($failedAttempts > 5) {
    lockAccount($username, 300); // 5-minute lockout
}
```

### File Upload Protection
```php
// File type validation
$allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
if (!in_array($fileType, $allowedTypes)) {
    throw new Exception('Invalid file type');
}

// File size limitation
if ($fileSize > MAX_FILE_SIZE) {
    throw new Exception('File too large');
}
```

---

## 🔧 Tools and Techniques

### Manual Testing Tools
- **Browser Developer Tools**: Inspect requests, modify parameters, analyze responses
- **Burp Suite**: Comprehensive web application security testing platform
- **OWASP ZAP**: Open-source web application security scanner
- **curl/wget**: Command-line HTTP clients for request manipulation

### Custom Scripts and Automation
- **Python Scripts**: Automated brute force and enumeration tools
- **SQL Injection Payloads**: Customized injection strings for database exploitation
- **XSS Vectors**: JavaScript payloads for cross-site scripting attacks
- **Path Traversal Lists**: Directory traversal payload collections

### Security Assessment Framework
```python
# Example security testing framework
class SecurityTest:
    def __init__(self, target_url):
        self.target = target_url
        self.vulnerabilities = []
    
    def test_sql_injection(self, parameter):
        payloads = ["'", "1' OR '1'='1", "1 UNION SELECT NULL--"]
        for payload in payloads:
            if self.check_sql_error(parameter, payload):
                self.vulnerabilities.append(f"SQL Injection in {parameter}")
    
    def test_xss(self, parameter):
        payload = "<script>alert('XSS')</script>"
        if payload in self.get_response(parameter, payload):
            self.vulnerabilities.append(f"XSS in {parameter}")
```

---

## 📊 Vulnerability Assessment Report

### Critical Vulnerabilities (High Priority)
- **SQL Injection**: Complete database compromise possible
- **File Upload**: Remote code execution potential
- **Path Traversal**: System file access and information disclosure

### High Vulnerabilities (Medium Priority)
- **Cross-Site Scripting**: Session hijacking and user impersonation
- **Authentication Bypass**: Unauthorized access to admin functions
- **Brute Force**: Account enumeration and credential compromise

### Medium Vulnerabilities (Low Priority)
- **Information Disclosure**: Sensitive data exposure
- **Header Manipulation**: Access control bypass
- **Open Redirect**: Phishing and social engineering attacks

### Remediation Timeline
1. **Immediate (0-7 days)**: Fix critical SQL injection and RCE vulnerabilities
2. **Short-term (1-4 weeks)**: Implement input validation and authentication controls
3. **Long-term (1-3 months)**: Security architecture review and comprehensive testing

---

## ⚠️ Ethical Use Disclaimer

**This project is intended for educational purposes only.** All techniques and vulnerabilities demonstrated should only be used in authorized testing environments or on systems you own.

### Responsible Disclosure
- **Never test on systems without explicit permission**
- **Use knowledge gained for defensive purposes**
- **Report vulnerabilities through proper channels**
- **Respect privacy and confidentiality**

### Legal Considerations
- **Unauthorized testing may violate laws and regulations**
- **Always obtain written permission before testing**
- **Follow your organization's security policies**
- **Consider the ethical implications of security research**

---

## 🏆 Project Status

**Status**: ✅ **Complete Educational Security Framework**

This 42 Darkly implementation successfully provides:
- ✅ **Comprehensive vulnerability coverage** spanning OWASP Top 10 categories
- ✅ **Practical exploitation techniques** with working proof-of-concepts
- ✅ **Educational documentation** explaining attack methodologies
- ✅ **Real-world relevance** with industry-standard attack vectors
- ✅ **Hands-on learning environment** for security skill development
- ✅ **Detailed remediation guidance** for defensive implementation

The project serves as an invaluable resource for cybersecurity education, providing practical experience with web application security testing in a controlled, ethical environment.

---

**42 School Security Project** | **Web Application Penetration Testing** | **Cybersecurity Education**

*This project demonstrates the importance of security-conscious development and provides essential hands-on experience for aspiring cybersecurity professionals.*

