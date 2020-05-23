from selenium import webdriver


driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/countries-of-north-america.html")

driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000)","")

