from faker import Faker
from locators import Locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

faker = Faker()

class TestRegistration:
    def test_registration(self, driver):
        email = faker.email()
        password = '123456'
        name = 'JulSSitn'
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.CONFIRM_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        assert '/login' in driver.current_url

    def test_registration_fail_password(self, driver):
        email = 'TEST_EMAIL'
        password = '123'
        name = 'Юлия33'
        driver.find_element(*Locators.ENTER_PROFILE_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.CONFIRM_REGISTRATION_BUTTON).click()
        error = driver.find_element(*Locators.ERROR_AUTH).text
        assert error == 'Некорректный пароль'


