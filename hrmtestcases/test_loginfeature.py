from time import sleep
import pytest
from conftest import *
from hrmpages.Loginpage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_login:


    def setup_class(self):
        self.driver.maximize_window()
        sleep(2)
        self.driver.get(BaseURL)
        self.login_page = LoginPage(self.driver)


    def test_valid_login(self):
        self.login_page.login(Username, Password)

    def test_pim_click(self):
        self.login_page.pimadd(Firstname,Lastname)

    def test_pim_details(self):
        self.login_page.pimempdetails(Licence,Licence_expdate,SSNnumber,DOB)

    def test_pim_edit(self):
        self.login_page.pimempedit(OtherID)

    def test_pim_delete(self):
        self.login_page.pimempdelete()

    def test_invalid_login(self):
        self.login_page.invalidlogin(Username, InvalidPwd)

    def teardown_class(self):
        self.driver.quit()
