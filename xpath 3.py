from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
'''
#self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/self::a").text
# print(text_msg)

# #parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/parent::td").text
# print(text_msg)
#
#child
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/child::td").text
#print(text_msg)

#driver.close()
'''
#length of nodes
# childs=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr/child::td")
# print(len(childs))


#Ancestor

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys')]/ancestor::tr").text
# print(text_msg)

#Decendant
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'RTCL Ltd.')]/ancestor::tr/desedant::*").text
# print(text_msg)

#followind
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'RTCL Ltd.')]/ancestor::tr/following::*")
print(len(text_msg))
#following -siblings
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'RTCL Ltd.')]/ancestor::tr/desedant::*").text
print(text_msg)

driver.close()
