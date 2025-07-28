import pytest
import allure
from pages.register_page import RegisterPage
import time
import random

@allure.title("Register New User and Delete Account")
@allure.description("Registers a new user and deletes the account to clean up")
@pytest.mark.usefixtures("setup")
class TestRegister:

    def test_register_user(self):
        register = RegisterPage(self.driver)
        random_email = f"testuser{random.randint(1000,9999)}@example.com"
        register.register_new_user("Shalini", random_email, "Test@1234")
        time.sleep(2)  # Optional wait to observe final step
