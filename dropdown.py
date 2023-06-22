from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

dropcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
##drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
#
# #3.select option from the dropdown
dropcountry_ele .select_by_visible_text("India")
# drpcountry.select_by_value("10")
# drpcountry.select_by_index(13)
#
#
#
#
# #capture all the option and print them
# alloptions=drpcountry.options
# print("total number of options:::",len(alloption))
#
#
# for opt in alloptions:
#     print(opt.text)
#
# #select option from dropdown without using built-in method
# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break
#
#
#
# alloptions=driver.driver.find_element(By.XPATH,"//select[@id='input-country']/option")
# print(len(alloptions))
