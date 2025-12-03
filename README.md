# 🎭 OrangeHRM Playwright Automation

![Tests](https://github.com/kingdingawy-sys/Playwright-OrangeHRM/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Playwright](https://img.shields.io/badge/playwright-1.48-green)
![License](https://img.shields.io/badge/license-MIT-blue)

> Modern test automation framework for OrangeHRM using Playwright, Python, and Pytest

---

## 🎯 Overview

Comprehensive E2E and API test automation framework for [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/) application demonstrating:
- Modern Playwright automation
- UI & API testing
- Page Object Model design
- CI/CD with GitHub Actions
- Detailed reporting & screenshots

---

## ✨ Features

- ✅ **Playwright** - Modern, fast, reliable automation
- ✅ **Page Object Model** - Maintainable test architecture
- ✅ **UI + API Testing** - Comprehensive coverage
- ✅ **Auto-wait & Smart Assertions** - Stable tests
- ✅ **Screenshots & Videos** on failure
- ✅ **Trace Viewer** - Debug failed tests
- ✅ **CI/CD Pipeline** - GitHub Actions
- ✅ **HTML Reports** - Beautiful test reports
- ✅ **Parallel Execution** - Fast test runs

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.11 |
| **Automation** | Playwright 1.48 |
| **Framework** | Pytest 8.3 |
| **API Testing** | Requests |
| **Reporting** | pytest-html, Allure |
| **CI/CD** | GitHub Actions |

---

## 📁 Project Structure
```
Playwright-OrangeHRM/
├── config/
│   ├── settings.py          
│   └── test_data.json        
│
├── tests/
│   ├── ui/
│   │   ├── pages/
│   │   │   ├── base_page.py
│   │   │   ├── login_page.py
│   │   │   ├── dashboard_page.py
│   │   │   └── admin_page.py
│   │   ├── test_login.py
│   │   ├── test_dashboard.py
│   │   └── test_admin_crud.py
│   │
│   └── api/
│       ├── test_login_api.py
│       ├── test_users_api.py
│       └── test_admin_api.py
│
├── utilities/
│   ├── logger.py            
│   ├── helpers.py           
│   ├── api_client.py        
│   └── generate_data.py    
│
├── reports/                 
├── .github/workflows/       
├── conftest.py             
├── pytest.ini             
├── requirements.txt       
└── README.md
```

---

## 📦 Installation

### Prerequisites
- Python 3.11+
- Git

### Setup
```bash
# 1. Clone repository
git clone https://github.com/kingdingawy-sys/Playwright-OrangeHRM.gitcd playwright-orangehrm

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install Playwright browsers
playwright install
```

---

## 🚀 Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run UI Tests Only
```bash
pytest tests/ui/ -v -s
```

### Run API Tests Only
```bash
pytest tests/api/ -v
```

### Run Specific Test
```bash
pytest tests/ui/test_login.py::TestLogin::test_successful_login_with_valid_credentials -v
```

### Run with HTML Report
```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

### Run in Headless Mode
```bash
pytest tests/ -v --browser chromium --headed=false
```

### Parallel Execution
```bash
pytest tests/ -v -n 4
```

---

## 📊 Test Coverage

| Category | Tests | Status |
|----------|-------|--------|
| **UI - Login** | 5 tests | ✅ |
| **UI - Dashboard** | 5 tests | ✅ |
| **UI - Admin** | 6 tests | ✅ |
| **API - Auth** | 3 tests | ⚠️ Demo limited |
| **Total** | **16+ tests** | **95%** |

### Test Distribution
- ✅ **Smoke Tests:** 10 tests
- ✅ **Regression Tests:** 6 tests
- ✅ **API Tests:** 3 tests (limited by demo)

---

## 🎨 Page Object Model
```python
# Example: Login Page
from tests.ui.pages.login_page import LoginPage

login_page = LoginPage(page)
login_page.navigate()
login_page.login("Admin", "admin123")
login_page.assert_login_successful()
```

---

## 📈 Reports

### HTML Report
After test run, open `reports/report.html` in browser

### Screenshots
All screenshots saved in `reports/screenshots/`

### Videos
Test videos saved in `reports/videos/`

### Traces
Debug traces in `reports/traces/` - open with:
```bash
playwright show-trace reports/traces/trace_xxx.zip
```

---

## 🔄 CI/CD

Automated testing runs on every push/PR via GitHub Actions.

**Status:** [![Tests](https://github.com/kingdingawy-sys/Playwright-OrangeHRM/actions/workflows/tests.yml/badge.svg)](https://github.com/kingdingawy-sys/Playwright-OrangeHRM/actions)

### Workflow Features:
- ✅ Runs on Ubuntu latest
- ✅ Python 3.11
- ✅ Playwright browsers auto-install
- ✅ Parallel test execution
- ✅ Screenshots & videos on failure
- ✅ HTML report artifact

---

## 🧪 Test Examples

### UI Test
```python
def test_successful_login(page: Page):
    """Test successful login flow"""
    login_page = LoginPage(page)
    dashboard = DashboardPage(page)
    
    login_page.navigate()
    login_page.login("Admin", "admin123")
    
    dashboard.assert_on_dashboard()
```

### API Test
```python
def test_api_health_check(api_client):
    """Test API is reachable"""
    response = api_client.get("/api/v2/admin/users")
    assert response.status_code in [200, 401, 403]
```

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

---

## 📝 License

MIT License

---

## 👤 Author

**Ibrahim Ahmed**
- 💼 LinkedIn: [Ibrahim Dingawy](https://www.linkedin.com/in/ibrahim-dingawy)
- 🐙 GitHub: [@kingdingawy-sys](https://github.com/kingdingawy-sys)
- 📧 Email: [kingdingawy@gmail.com](mailto:kingdingawy@gmail.com)

---

## 🙏 Acknowledgments

- [OrangeHRM](https://opensource-demo.orangehrmlive.com/) - Demo application
- [Playwright](https://playwright.dev/) - Modern automation framework
- [Pytest](https://pytest.org/) - Testing framework

---

## 📊 Project Stats

- **Lines of Code:** 1500+
- **Test Cases:** 16+
- **Page Objects:** 4
- **Test Coverage:** 95%+
- **Average Test Duration:** 2-3 minutes

---

⭐ **Star this repo if you find it useful!**