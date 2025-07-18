from selenium.webdriver.common.by import By

class AuthPageLocators:
   username_input = [By.ID, "username"]
   password_input = [By.XPATH, "//form[@id='login-form']//input[@type='password']"]
   login_button = [By.ID, "login-button"]
   confirm_button = [By.ID, "login-otp-button"]
   login_error = [By.XPATH, "//div[@data-key='invalidOtpCode']"]