from selenium.webdriver.common.by import By
from time import sleep
from hrmhelpers.Selenium_helper import Selenium_Helper


# noinspection PyInterpreter
class LoginPage(Selenium_Helper):
    email_ele = (By.XPATH,"//input[@name='username']")
    password_ele = (By.XPATH,"//input[@name='password']")
    login_ele = (By.XPATH,"//button")
    pim_ele = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
    admin_ele = (By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i")
    addemp_ele = (By.LINK_TEXT, "Add Employee")
    firstname_ele = (By.XPATH,"//input[@name='firstName']")
    lastname_ele = (By.XPATH, "//input[@name='lastName']")
    create_ele = (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
    licence_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
    licenceexp_ele = (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input")
    ssn_ele = (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input")
    nationality_ele = (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]")
    marital_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]")
    gender_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span")
    dob_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input")
    military_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input")
    employeelist_ele=(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
    otherid_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input")
    save_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button")
    employeeid_ele =(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
    search_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    checkbox_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span")
    delete_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i")
    edit_ele=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]")

    def __init__(self,driver):
        super().__init__(driver)
    #doing a valid login
    def login(self,username,password):
        self.webelement_enter(self.email_ele,username)
        self.webelement_enter(self.password_ele,password)
        self.webelement_click(self.login_ele)
        sleep(2)

    #adding a new employee
    def pimadd(self,firstname,lastname):
        self.webelement_click(self.pim_ele)
        self.webelement_click(self.addemp_ele)
        sleep(2)
        self.webelement_enter(self.firstname_ele, firstname)
        self.webelement_enter(self.lastname_ele, lastname)
        input = self.driver.find_element(by=By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
        self.emp_id = input.get_attribute('value')
        sleep(2)
        self.webelement_click(self.create_ele)
        sleep(5)

    #entering employee personal details
    def pimempdetails(self, licence, licexp, ssn, dob):
        self.webelement_enter(self.licence_ele,licence)
        sleep(2)
        self.webelement_enter(self.licenceexp_ele, licexp)
        sleep(3)
        # self.webelement_enter(self.ssn_ele, ssn)
        # sleep(2)
        self.driver.execute_script("window.scrollBy(0,300)", "")
        sleep(2)
        self.driver.find_element(by=By.XPATH,value="(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'][1])").click()
        # Click on ESS element
        self.driver.find_element(by=By.XPATH, value="(//div[@role='listbox']//child::div)[5]").click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]").click()
        # Click on ESS element
        self.driver.find_element(by=By.XPATH, value="(//div[@role='listbox']//child::div)[3]").click()
        sleep(2)
        self.webelement_enter(self.dob_ele, dob)
        sleep(2)
        self.webelement_click(self.gender_ele)
        sleep(2)
        # self.webelement_enter(self.military_ele, self.emp_id)
        # sleep(2)
        self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]").click()
        # Click on ESS element
        self.driver.find_element(by=By.XPATH, value="(//div[@role='listbox']//child::div)[4]").click()
        sleep(2)
        self.webelement_click(self.save_ele)
        sleep(4)

    #editing the personal details of the added employee and updating otherid field
    def pimempedit(self,otherid):
        self.webelement_click(self.employeelist_ele)
        sleep(4)
        self.webelement_click(self.employeelist_ele)
        sleep(2)
        self.webelement_enter(self.employeeid_ele, self.emp_id)
        sleep(2)
        self.webelement_click(self.search_ele)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        sleep(2)
        self.webelement_click(self.checkbox_ele)
        sleep(2)
        self.webelement_click(self.edit_ele)
        sleep(2)
        self.webelement_enter(self.otherid_ele, otherid)
        sleep(3)
        self.webelement_click(self.save_ele)
        sleep(4)



    #deleting the newly added employee details
    def pimempdelete(self):
        self.webelement_click(self.employeelist_ele)
        sleep(2)
        self.webelement_enter(self.employeeid_ele, self.emp_id)
        sleep(2)
        self.webelement_click(self.search_ele)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        sleep(2)
        self.webelement_click(self.checkbox_ele)
        sleep(2)
        self.webelement_click(self.delete_ele)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        sleep(2)


    #logout and passing invalid login details
    def invalidlogin(self, username, password):
        # self.webelement_click(self.admin_ele)
        # sleep(3)
        self.driver.find_element(by=By.XPATH,value="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span").click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()
        sleep(2)
        self.webelement_enter(self.email_ele, username)
        self.webelement_enter(self.password_ele, password)
        self.webelement_click(self.login_ele)
        sleep(4)














