from selenium import webdriver
from selenium.webdriver.common.by import By

dglweb=webdriver.Chrome()
dglweb.get('https://testweb.daguanlian.com')
dglweb.maximize_window()
dglweb.find_element_by_xpath("//a[@class='fl wd_fff fs12 pointer']").click()



#关闭当前窗口
dglweb.close()

#关闭所有打开的窗口
#dglweb.quit()



