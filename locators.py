from selenium.webdriver.common.by import By

class Locators:
    ENTER_PROFILE_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # селектор кнопки Личный кабинет
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")  # селектор кнопки зарегистрироваться
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::*") #селектор поля ввода имени
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # селектор поля ввода email
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")  #селектор поля ввода пароля
    CONFIRM_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #селектор кнопки подтверждения регистрации
    ENTRANCE_HEADER = (By.XPATH, ".//h2[text()='Вход']")  # селектор заголовка формы логина
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # селектор кнопки входа на форме логина
    ERROR_AUTH = (By.XPATH, "//div/main/div/form/fieldset[3]/div/p") #селектор ошибки авторизации

    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") #селектор кнопки Войти в аккаунт
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") #селектор кнопки Оформить заказ
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") #селектор кнопки Восстановить пароль
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']") #селектор заголовка формы восстановления пароля
    ENTER_ACCOUNT_FROM_RESTORE_FORM_BUTTON = (By.XPATH, "//a[text()='Войти']") #селектор кнопки Войти из формы восстановления пароля
    HEADER_ACCOUNT_PROFILE = (By.XPATH, ".//a[@href='/account/profile']") #селектор заголовка в Личном кабинете
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")  #селектор кнопки выхода из аккаунта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']") #селектор кнопки Конструктор
    LOGO_ST = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']") #селектор Логотипа
    BUILD_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']") #селектор заголовка Соберите бургер
    BUTTON_SAUCES = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']") #вкладка Соусы
    BUTTON_FILLINGS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']")#вкладка Начинки
    BUTTON_BUNS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']") #вкладка Булки
    HEADER_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")#заголовок вкладки Соусы
    HEADER_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")#заголовок вкладки Начинки
    HEADER_BUNS = (By.XPATH, ".//h2[text()='Булки']")#заголовок вкладки Булки




