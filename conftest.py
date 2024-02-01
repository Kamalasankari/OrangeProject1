from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


BaseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"
InvalidPwd = "Invalid Password"
Firstname = "Kamalasankari"
Lastname = "Muthappan"
Licence = "123456"
Licence_expdate = "2025-06-01"
SSNnumber="67890"
DOB = "1982-03-06"
OtherID = "1111"


@pytest.fixture(scope="class", autouse = True)
def browser_setup(request):
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    # noinspection PyTypeHints
    config.option.htmlpath: Path = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "HRM Test Reports"



