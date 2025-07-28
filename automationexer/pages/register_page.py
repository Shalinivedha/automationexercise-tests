from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):

    SIGNUP_LOGIN = (By.LINK_TEXT, "Signup / Login")
    NEW_USER_TEXT = (By.XPATH, "//h2[text()='New User Signup!']")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    ENTER_ACCOUNT_INFO = (By.XPATH, "//b[text()='Enter Account Information']")
    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    PARTNER_CHECKBOX = (By.ID, "optin")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    CREATE_ACCOUNT = (By.XPATH, "//button[@data-qa='create-account']")

    ACCOUNT_CREATED = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    LOGGED_IN_AS = (By.XPATH, "//li[contains(text(),'Logged in as')]")
    DELETE_ACCOUNT = (By.LINK_TEXT, "Delete Account")
    ACCOUNT_DELETED = (By.XPATH, "//b[text()='Account Deleted!']")
    CONTINUE_AFTER_DELETE = (By.XPATH, "//a[@data-qa='continue-button']")

    def register_new_user(self, name, email, password):
        self.click(self.SIGNUP_LOGIN)
        self.is_visible(self.NEW_USER_TEXT)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)
        self.is_visible(self.ENTER_ACCOUNT_INFO)

        self.click(self.TITLE_MR)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.select_dropdown(self.DAYS, "10")
        self.select_dropdown(self.MONTHS, "May")
        self.select_dropdown(self.YEARS, "1994")

        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.PARTNER_CHECKBOX)

        self.enter_text(self.FIRST_NAME, "Shalini")
        self.enter_text(self.LAST_NAME, "P")
        self.enter_text(self.COMPANY, "MyCompany")
        self.enter_text(self.ADDRESS1, "No.123, Main Street")
        self.enter_text(self.ADDRESS2, "Flat 2B")
        self.select_dropdown(self.COUNTRY, "India")
        self.enter_text(self.STATE, "Tamil Nadu")
        self.enter_text(self.CITY, "Chennai")
        self.enter_text(self.ZIPCODE, "600001")
        self.enter_text(self.MOBILE, "9876543210")

        self.click(self.CREATE_ACCOUNT)
        self.is_visible(self.ACCOUNT_CREATED)
        self.click(self.CONTINUE_BUTTON)
        self.is_visible(self.LOGGED_IN_AS)

        self.click(self.DELETE_ACCOUNT)
        self.is_visible(self.ACCOUNT_DELETED)
        self.click(self.CONTINUE_AFTER_DELETE)
