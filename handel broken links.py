import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0

for link in alllinks:
    url=link.get_attribute("href")
    res=requests.head(url)
    if res.status_code>=400:
        print(url,"   is broken link   ")
        count+=1
    else:
        print(url," is valid link  ")
print("Tptal number of broken links",count)