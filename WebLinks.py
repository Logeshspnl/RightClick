from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

links=driver.find_elements(By.TAG_NAME,("a"))

print("Number of links:",len(links))

for link in links:

    print(link.text)
        