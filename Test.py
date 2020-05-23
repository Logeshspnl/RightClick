from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
driver.maximize_window()

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

driver.find_element_by_id("RESULT_RadioButton-7_0").click()

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

