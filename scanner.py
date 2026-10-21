
import requests
from urllib.parse import urlparse
from datetime import datetime

SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps control which resources a page can load.",
    "Strict-Transport-Security": "Helps browsers enforce HTTPS.",
    "X-Content-Type-Options": "Helps prevent MIME-type sniffing.",
    "X-Frame-Options": "Helps protect against clickjacking.",
    "Referrer-Policy": "Controls referrer information."
}


def scan_website(url):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        print("Invalid URL.")
        return

    if parsed.username or parsed.password:
        print("URLs containing credentials are not allowed.")
        return

    findings = []

    try:
        response = requests.get(url, timeout=10)
        print("\nAUTOMATED WEB SECURITY SCANNER")
        print("=" * 40)
        print("HTTP status:", response.status_code)
        print("Final URL:", response.url)

        if urlparse(response.url).scheme == "https":
            findings.append("PASS: Final page uses HTTPS.")
        else:
            findings.append("REVIEW: Final page uses HTTP.")

        print("\nSECURITY HEADER CHECKS")
        print("-" * 40)

        for header, purpose in SECURITY_HEADERS.items():
            value = response.headers.get(header)

            if value:
                findings.append(f"PASS: {header} is present.")
            else:
                findings.append(
                    f"REVIEW: {header} is missing. {purpose}"
                )

        # Basic CORS observation using a test Origin
        test_origin = "https://scanner-test.invalid"

        cors_response = requests.get(
            url,
            timeout=10,
            headers={"Origin": test_origin}
        )

        allow_origin = cors_response.headers.get(
            "Access-Control-Allow-Origin", ""
        )

        if allow_origin == "*":
            findings.append(
                "REVIEW: CORS allows any origin; review whether "
                "this is appropriate for the resource."
            )
        elif allow_origin == test_origin:
            findings.append(
                "REVIEW: The test origin was allowed; verify "
                "whether it is trusted."
            )
        else:
            findings.append(
                "INFO: The test origin was not explicitly allowed."
            )

        print("\nSCAN RESULTS")
        print("-" * 40)

        for finding in findings:
            print(finding)

        with open("scan_report.txt", "w", encoding="utf-8") as report:
            report.write("AUTOMATED WEB SECURITY SCAN REPORT\n")
            report.write("=" * 40 + "\n")
            report.write(f"Requested URL: {url}\n")
            report.write(f"Final URL: {response.url}\n")
            report.write(f"HTTP status: {response.status_code}\n")
            report.write(f"Scan time: {datetime.now().isoformat()}\n\n")

            for finding in findings:
                report.write(f"{finding}\n")

            report.write(
                "\nLimitations: Basic configuration checks only. "
                "Findings require manual interpretation.\n"
            )

        print("\nReport saved as scan_report.txt")

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)


if __name__ == "__main__":
    target = input("Enter authorized website URL: ").strip()

    if "://" not in target:
        target = "https://" + target

    scan_website(target)
