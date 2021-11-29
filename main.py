from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from First_test import MainPage

driver = webdriver.Chrome(ChromeDriverManager().install())
main_page = MainPage(driver)
main_page.open()
assert "Яндекс" in driver.title
main_page.seacrh("Python")
assert "Python" in main_page.page_source()

main_page.quit()