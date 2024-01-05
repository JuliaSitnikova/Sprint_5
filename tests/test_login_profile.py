from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
class TestLogin:
    def test_login_profile_button(self, driver):

        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element_located(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

    def test_login_button_enter_account(self, driver):

        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

    def test_login_from_registration_form(self, driver):
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element_located(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

    def test_login_from_forgot_password(self, driver):
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.HEADER_RESTORE_PASSWORD))
        driver.find_element(*Locators.ENTER_ACCOUNT_FROM_RESTORE_FORM_BUTTON).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element_located(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()








