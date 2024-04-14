import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.avito.ru/")
driver.maximize_window()

link_signup = driver.find_element(By.XPATH, "//a[@data-marker='header/login-button']")
link_signup.click()

time.sleep(3)

user_name = driver.find_element(By.NAME, "login")
user_name.send_keys('test_new@mail.ru')
password = driver.find_element(By.NAME,"password")
password.send_keys('test_new')
button_submit = driver.find_element(By.NAME, "submit")
button_submit.click()

time.sleep(3)

link_polza = driver.find_element(By.XPATH, "//a[@href='/avito-care?from=mp_header']")
link_polza.click()

time.sleep(3)

#link_eco = driver.find_element(By.XPATH, "//a[@href='/avito-care/eco-impact?from=avito-care-navigation']")
link_eco = driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div[5]/span")
link_eco.click()

time.sleep(3)

element = driver.find_element(By.XPATH, "//div[@class='desktop-impact-items-F7T6E']")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

driver.get_screenshot_as_file('/Users/dilia/PycharmProjects/selenium_test1/pythonProject/output/2.png')
driver.quit()