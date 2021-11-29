from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://yandex.ru'

    def open(self):
        self.driver.get(self.url)

    def _search_input(self):
        return self.driver.find_element(By.ID,"text")


    def seacrh(self, item: str):
        self._search_input().clear()
        self._search_input().send_keys(item)
        self._search_input().send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10) # не совсем понял как пользоваться ожидаем, он ожидает до тех пор пока не выполнит запрос?

    def quit(self):
        self.driver.quit()

    def page_source(self) -> str:
        return self.driver.page_source
