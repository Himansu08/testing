import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/')
time.sleep(10)
driver.maximize_window()



#Absolute Xpath
# #
# driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[2]/div[2]/form/input').send_keys('Laptop')
# driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[2]/div[2]/form/button').click()

#Relative Xpath
# driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
driver.find_element((By.XPATH,'//button[@type="submit"]')).click()

#or Operator
# driver.find_element(By.XPATH, "//input[@id='small-searchterms' or @name='q']").send_keys("Laptop")
# driver.find_element(By.XPATH, "//input[@id='small-searchterms' or @name='q']").click()
# #search botton
# driver.find_element(By.XPATH, "//button[@type='submit' and @class='button-1 search-box-button']").send_keys("Laptop")
# driver.find_element(By.XPATH, "//button[@type='submit' and @class='button-1 search-box-button']").click()

#Contains   &start-with()
# driver.find_element(By.XPATH, "//input[contains(@type,"'submit'")]").send_keys("Laptop")
# driver.find_element(By.XPATH, "//input[starts-with(@type,"'submit'")]").click()


#text

# driver.find_element(By.XPATH, "//a[text()='Log in']").send_keys("Laptop")
# driver.find_element(By.XPATH, "//a[text()='Log in']").click()

#