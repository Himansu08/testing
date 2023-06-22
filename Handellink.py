from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#click on the link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element((By.PARTIAL_LINK_TEXT,'Digital')).click()

# #find all the link on the page
# links=driver.find_elements(By.TAG_NAME,"a")
links=driver.find_elements(By.XPATH,"//a")
print("total no of links",len(links))



#print all the link name
for link in links:
    print(link.text)