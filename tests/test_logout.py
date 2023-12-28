from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants

class TestLogout:
    def test_logout_from_account(self, driver):
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(Locators.ENTRANCE_HEADER))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed()

        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Constants.PROFILE_URL

        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == Constants.LOGIN_PAGE