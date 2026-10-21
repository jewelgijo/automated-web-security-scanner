# Automated Web Security Scanner Using Python

**Project Domain:** Cybersecurity – Web Application Security  
**Programming Language:** Python  
**Development Environment:** Visual Studio Code  
**Library Used:** Requests

## 1. Abstract

The Automated Web Security Scanner Using Python is a beginner-level cybersecurity project designed to perform preliminary checks of selected website security configurations.

The application sends HTTP requests to a specified website, examines important HTTP security headers, observes basic Cross-Origin Resource Sharing (CORS) behavior, and generates a text report containing the scan findings.

The project demonstrates how Python can be used to automate basic web security checks and organize the results for further investigation.

## 2. Introduction

Web application security is an important part of cybersecurity. Incorrect security configurations can increase the risk of attacks, depending on the application and its environment.

Manually reviewing selected HTTP response headers can be time-consuming. This project provides a simple automated tool that checks for the presence of selected security headers and reports configurations that may require further review.

The scanner is intended for educational purposes and preliminary security configuration assessment. It is not a replacement for a professional security audit or penetration test.

## 3. Problem Statement

Website security configurations need to be reviewed to identify settings that may require improvement. Manual inspection of HTTP response headers can be repetitive and may make it difficult for beginners to organize their observations.

This project addresses the problem by developing a Python-based tool that automates selected checks and generates a readable report.

## 4. Objectives

The main objectives of the project are:

1. To develop a basic automated web security scanner using Python.
2. To check whether the final page URL uses HTTPS.
3. To inspect selected HTTP security headers.
4. To observe basic CORS response behavior.
5. To display scan findings in the terminal.
6. To generate a text report containing the results.
7. To understand the importance and limitations of basic web security configuration checks.

## 5. Technologies Used

- **Python:** Implements the scanning logic.
- **Requests:** Sends HTTP requests and reads response headers.
- **Visual Studio Code:** Used to write and run the Python programs.
- **Python HTTP Server:** Creates a local test website for controlled testing.

## 6. System Requirements

### Hardware
- A computer or laptop
- Internet access for installing the required Python package, if needed

### Software
- Windows operating system
- Python 3
- Visual Studio Code
- Python Requests library

## 7. Security Checks Performed

The scanner checks the following items:

### 7.1 HTTPS Check
The scanner checks whether the final URL uses HTTPS. HTTPS helps protect data exchanged between a browser and a web server when properly configured.

### 7.2 Content-Security-Policy (CSP)
This header helps control which resources a browser is permitted to load and can reduce certain content injection risks.

### 7.3 Strict-Transport-Security (HSTS)
This header instructs supporting browsers to enforce HTTPS for a specified period, subject to the header configuration and browser behavior.

### 7.4 X-Content-Type-Options
This header can help prevent browsers from interpreting content as a different MIME type than the one declared by the server.

### 7.5 X-Frame-Options
This header provides a mechanism to restrict framing of a page and can help mitigate certain clickjacking attacks.

### 7.6 Referrer-Policy
This header controls how much referrer information browsers send during navigation and requests.

### 7.7 CORS Configuration Observation
The scanner sends a request containing a test Origin header and observes the Access-Control-Allow-Origin response header. A wildcard origin is flagged for review.

A wildcard CORS response is not automatically a vulnerability. Its significance depends on the resource, application behavior, and other access controls.

## 8. Methodology

The project follows these steps:

1. Accept a website URL from the user.
2. Validate the URL format.
3. Send an HTTP GET request using the Requests library.
4. Record the HTTP response status and final URL.
5. Check whether the final URL uses HTTPS.
6. Inspect the selected HTTP security headers.
7. Send a second request with a test Origin header.
8. Interpret the returned CORS header at a basic level.
9. Display the findings in the terminal.
10. Save the findings in `scan_report.txt`.

## 9. Project Files

The project contains the following files:

- `scanner.py` — Main Python scanning program.
- `test_server.py` — Local test website used to verify scanner behavior.
- `requirements.txt` — Lists the required Python package.
- `README.md` — Project documentation.
- `scan_report.txt` — Generated scan results.
- `screenshots/` — Screenshots of actual execution and test results.

## 10. Installation and Execution

### Step 1: Install Python
Install Python 3 and verify the installation:

```powershell
python --version
```

### Step 2: Create a Virtual Environment

```powershell
python -m venv venv
```

Activate the environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

The `requirements.txt` file contains:

```text
requests
```

Install the dependency:

```powershell
python -m pip install -r requirements.txt
```

### Step 4: Start the Local Test Website

In one terminal, run:

```powershell
python test_server.py
```

The local test server listens at:

`http://127.0.0.1:8000`

Keep the server running while performing the test.

### Step 5: Run the Scanner

Open another terminal and run:

```powershell
python scanner.py
```

When prompted, enter the authorized target URL:

`http://127.0.0.1:8000`

### Step 6: View the Report

After the scan completes, open `scan_report.txt` in the project folder.

## 11. Testing and Observed Results

The scanner was tested against a local test website running on the same computer.

The observed report included:

- HTTP status code: 200
- Final URL: `http://127.0.0.1:8000/`
- Content-Security-Policy: Present
- X-Content-Type-Options: Present
- Strict-Transport-Security: Missing
- X-Frame-Options: Missing
- Referrer-Policy: Missing
- CORS: Wildcard origin observed

The HTTP response status of 200 indicated that the local test server responded successfully.

The missing headers were reported for further review. The CORS observation indicated that the test server allowed any origin in its response.

These results describe the configured local test server. They do not establish that a public website is vulnerable.

## 12. Limitations

The project has the following limitations:

1. It checks only a limited set of HTTP security configurations.
2. Missing security headers do not automatically prove a vulnerability.
3. CORS behavior requires contextual interpretation.
4. The scanner does not perform exploit testing or penetration testing.
5. It does not inspect