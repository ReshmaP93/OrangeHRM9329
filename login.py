import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)

driver.get("https://reshmapeddeti93-trials79.orangehrmlive.com/auth/seamlessLogin")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("fC28rM@ENm")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
driver.close()
