import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

dgldriver = webdriver.Chrome()
dgldriver.get('https://testadmin.daguanlian.com')
nameele = dgldriver.find_element_by_name('name')
nameele.click()
nameele.send_keys('admin')
passele = dgldriver.find_element_by_name('password')
passele.click()
passele.send_keys('111111')
subele = dgldriver.find_element_by_xpath("//button[@class='login_btn width240']")
subele.click()
time.sleep(2)
dgldriver.maximize_window()
WebDriverWait(dgldriver, 0.5).until(EC.presence_of_element_located((By.ID, "userName")))
print(dgldriver.find_element_by_id("userName").text)


"""
try:
    WebDriverWait(dgldriver, 0.5).until(EC.presence_of_element_located((By.ID, "userName")))
    
    assert dgldriver.find_element_by_id("userName").text == '平台超管'
    
finally:
    dgldriver.close()
"""



#assert workele.text '工作台'






