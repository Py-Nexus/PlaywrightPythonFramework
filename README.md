# 🔍 UI Test Automation Framework

A scalable and maintainable UI test automation framework built using **Python**, **Playwright**, **Pytest**, and integrated with **ReportPortal.io** for real-time test reporting. Developed and maintained using **PyCharm IDE**.

---

## 🛠️ Tech Stack

| Component        | Description                                     |
|------------------|-------------------------------------------------|
| **Language**     | Python 3.7+                                     |
| **Automation**   | Playwright (browser automation)                 |
| **Test Runner**  | Pytest                                          |
| **Reporting**    | ReportPortal.io (test analytics and dashboards) |
| **IDE**          | PyCharm (recommended for development)           |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/Py-Nexus/PlaywrightPythonFramework

### 2️⃣ Set Up Python Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt
playwright install

### 4️⃣ Configure ReportPortal
rp_uuid = <your_user_token>
rp_endpoint = https://<your_reportportal_url>/api/v1
rp_project = <your_project_name>
rp_launch = Playwright Python Run
rp_enable = True

## 🚀 Running Tests
### Basic Test Run
pytest
### Run with ReportPortal Enabled
pytest --reportportal
### Run Specific Tests
pytest tests/test_example.py::test_open_google
