# NetGuard-CI: Secure Network Monitor
NetGuard is a containerized python-based monitoring tool to track network availability on websites. This project demonstrates Secure Software Development Lifecycle 

Prequisites
* Docker Desktop installed
  
How It Works
*NetGuard-CI uses a DevSecOps pipeline to ensure that every update to the monitor is safe and stable
*Automated Auditing: Every "Push" to this repository triggers a GitHub Actions workflow that runs a gauntlet
* Secret Detection: Trufflehob scans the code to ensure no API keys or sensetive credentials get leake
* Infrastructure linting: Hadolint checks the Dockerfile to ensure it follows industry-standard security configuration
* Vulerability Scanning: Trivy audits the Python environment and container filesystem for known vulnerabilities


Usage
Build Docker docker build -t netguard-ci .

Paste targets URl
docker run --env MONITOR_TARGETS="https://google.com,https://github.com" netguard-ci




