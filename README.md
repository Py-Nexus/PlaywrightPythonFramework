# 🤖 UI Test Automation Framework

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![ReportPortal](https://img.shields.io/badge/ReportPortal.io-FF6F00?style=for-the-badge&logo=datadog&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-21D789?style=for-the-badge&logo=pycharm&logoColor=white)
![GitHub Repo stars](https://img.shields.io/github/stars/Py-Nexus/PlaywrightPythonFramework?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/Py-Nexus/PlaywrightPythonFramework?style=for-the-badge)
> A scalable and maintainable UI test automation framework built using **Python**, **Playwright**, **Pytest**, and integrated with **ReportPortal.io** for real-time test reporting. Developed and maintained using **PyCharm IDE**. **Docker** support is included for easy setup and execution.
---

## 🛠️ Tech Stack

| Component        | Description                                     |
|------------------|-------------------------------------------------|
| **Language**     | Python 3.7+                                     |
| **Automation**   | Playwright (browser automation)                 |
| **Test Runner**  | Pytest                                          |
| **Reporting**    | ReportPortal.io (test analytics and dashboards) |
| **IDE**          | PyCharm (recommended for development)           |
| **Container**    | Docker (for isolated, reproducible runs)        |

---
## ✨ Why This Framework?
- **Cross-browser testing** powered by Playwright (Chromium, Firefox, WebKit)
- **Real-time test analytics** with ReportPortal.io
- **Containerized execution** via Docker
- **Easily maintainable structure** with reusable utilities & fixtures
- **Supports CI/CD pipelines** out of the box
---
### 📂 Project Structure
```bash
PlaywrightPythonFramework/
│── configdata/         # Test URLs and locators 
│── pages/              # Page object models
│── testcases/          # Test cases
│── utilities/          # Helper functions
│── .gitignore          # Git ignore file
│── docker-compose.yaml # Docker Compose config
│── Dockerfile          # Docker config
│── pytest.ini          # Pytest and ReportPortal config
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Py-Nexus/PlaywrightPythonFramework.git
```

### 2️⃣ Set Up Python Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4️⃣ Configure ReportPortal
```bash
rp_api_key = <your_api_key_here>
rp_endpoint = https://<your_reportportal_url>
rp_project = <your_project_name>
rp_launch = Playwright Python Run
rp_enable = True
```

## 🚀 Running Tests
### 🧪 Basic Test Run
```bash
pytest
```
### 📊 Run with ReportPortal Enabled
```bash
pytest --reportportal
```
### 🐳📊 Run with ReportPortal Enabled (Docker)
```bash
docker compose run --rm playwright-python-framework
```
### 🎯 Run Specific Tests
```bash
pytest tests/test_example.py::test_open_google
```
### 🐳🎯 Run Specific Tests (Docker)
```bash
docker compose run --rm playwright-python-framework pytest tests/test_example.py::test_open_google
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repo 🍴
2. Create a feature branch 💡
3. Submit a PR 🚀

---

## 📄 License

MIT License. Feel free to use and share.

> Made with 🤖✅ by [Kunal](https://github.com/Py-Nexus) and [Amit](https://github.com/amit-automationQA)
