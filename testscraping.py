import imp
from lib2to3.pgen2 import driver
from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("https://thisupplyden.com/account/login")
    e = driver.find_element(By.NAME, "customer[email]")
    e.send_keys("rifqi.testing@yopmail.com")
    e = driver.find_element(By.NAME, "customer[password]")
    e.send_keys("123654qq!")
    e = driver.find_element(By.CLASS_NAME, "login-button")
    e.click()
finally:
    print("user berhasil login")