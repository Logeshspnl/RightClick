from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")

driver.get("https://www.toolsqa.com/automation-practice-table/")

rows = len(driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[2]/div[1]/div[1]/table/tbody/tr"))#finding no of rows
cols = len(driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[2]/div[1]/div[1]/table/tbody/tr/td"))#finding no of cols

print(rows)
print(cols)

for r in range(1,rows+1):
    for c in range(1,cols):
        value = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[2]/div[1]/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value)

    print()
    time.sleep(2)



