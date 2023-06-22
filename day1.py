# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
#
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get('http://opensourcce-demo.orangehrmlive.com/')
# driver.find_element_by_name("teUsername").send_key("Admin")
# driver.find_element_by_id('txPassword').send_keys("admin123")
# driver.find_element_by("btnLogin").click()
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver .close()

# Locator
# (id,name,Linktext PartialLinktext,Class Name,TagName)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://demo.nopcommerce.com/")
