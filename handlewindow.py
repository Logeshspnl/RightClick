from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()

print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:

    driver.switch_to_window(handle)
    print(driver.title)

driver.close()