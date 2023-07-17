from selenium.webdriver.common.by import By


class HomePageLocators:
    login_button = By.XPATH, '//*[contains(text(), "Войти в аккаунт")]'  # Кнопка войти в аккаунт
    place_order_button = By.XPATH, '//*[contains(text(), "Оформить заказ")]'  # Кнопка оформить заказ
    personal_account_button_text_header = (By.XPATH, './/nav/a/p')  # Кнопка личный кабинет в хэдере
    collect_burger_text = (By.XPATH, "//button[contains(text(), 'Соберите бургер')]")  # Надпись Соберите бургер в конструкторе
    sauces_button = By.XPATH, '//span[contains(text(), "Соусы")]'  # Кнопка соусы
    sauce_third = (By.XPATH, './/p[contains(text(), "Соус традиционный галактический")]')  # Третий соус в разделе соусов
    bulki_button = By.XPATH, '//span[contains(text(), "Булки")]'  # Кнопка Булки
    bulki_second = (By.XPATH, './/p[contains(text(), "Краторная булка N-200i")]')  # Вторая булка в разделе булок
    filling_button = By.XPATH, '//span[contains(text(), "Начинки")]'  # Кнопка начинки
    filling_second_ingredient = (By.XPATH, './/p[contains(text(), "Мясо бессмертных моллюсков Protostomia")]')  # Вторая начинка в разделе начинок


class AuthorizationLocators:
    email_authorization = (By.XPATH, "//input[@type='text']")
    password_input = (By.XPATH, "//input[@type='password']")
    button_text_registration = By.XPATH, '//a[contains(text(), "Зарегистрироваться")]'  # Кнопка зарегистрироваться
    button_text_forgot_password = By.LINK_TEXT, 'Восстановить пароль'  # Восстановить пароль
    password_authorization = (By.XPATH, './/input[(@name="Пароль")]')  # Поле ввода пароля в разделе логина
    button_enter = By.XPATH, '// *[contains(text(), "Войти")]'  # Кнопка "Войти"
    text_enter = By.XPATH, '// *[contains(text(), "Вход")]'  # Надпись Вход


class RegistrationLocators:
    name_registration = (By.NAME, 'name')  # Поле ввода имени в форме регистрации
    email_registration = By.XPATH, '//*[text()="Email"]/following-sibling::input'  # Поле ввода email в форме регистрации
    password_registration = (By.XPATH, './/input[(@name="Пароль")]')  # Поле ввода пароля в форме регистрации
    button_registration = (By.XPATH, './/form/button')  # Кнопка регистрации
    wrong_password_text = By.XPATH, '//*[contains(text(), "Некорректный пароль")]'  # Надпись некорректный пароль
    button_text_enter = (By.XPATH, './/p/a')  # Кнопка войти
    small_password = (By.XPATH, "//input[@type='password']")


class PersonalAccountLocators:
    text_change_personal_data = (
        By.XPATH, './/nav/p[(text() = "В этом разделе вы можете изменить свои персональные данные")]')
    # Надпись в аккаунте Вы можете изменить свои данные
    button_text_constructor_header = By.XPATH, '//p[contains(text(), "Конструктор")]'  # кнопка конструктор в хэдере
    logout_button = (By.XPATH, './/ul/li/button')  # кнопка выйти
