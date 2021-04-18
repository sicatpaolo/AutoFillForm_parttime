from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'D:\Work\Python\chromedriver_win32\chromedriver.exe')
#
#function for logging in

def login(barrier1, email, password, submit):
    time.sleep(5)
    driver.find_element_by_xpath(barrier1).click()
    time.sleep(5)
    driver.find_element_by_xpath(email).send_keys("username") # Change username
    driver.find_element_by_xpath(password).send_keys("pass123") # Change password
    time.sleep(5)
    driver.find_element_by_xpath(submit).click()
    time.sleep(5)
