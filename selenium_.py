from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://freelancer.com.br/')
time.sleep(10)

driver.maximize_window()

driver.quit()