from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants

class TestTransitionProfile:
    def test_transition_to_profile(self, driver):
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element_located(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Constants.PROFILE_URL

    def test_transition_to_constructor(self, driver):
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element_located(Locators.ENTRANCE_HEADER))
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))

        assert driver.current_url == Constants.URL

    def test_transition_to_logo(self, driver):
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element_located(Locators.ENTRANCE_HEADER))
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        driver.find_element(*Locators.LOGO_ST).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))

        assert driver.current_url == Constants.URL












