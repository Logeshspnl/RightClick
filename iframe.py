from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")

driver.get("https://selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")

driver.find_element_by_link_text("com.thoughtworks.selenium").click()

driver.switch_to_default_content()

driver.switch_to_frame("packageFrame")

driver.find_element_by_link_text("AbstractAnnotations").click()

driver.switch_to_default_content()

