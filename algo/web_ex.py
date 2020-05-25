from selenium import webdriver
import time

# 打开网页
website = webdriver.Chrome()
dgl_url= "https://testweb.daguanlian.com"
test_url = "http://bbs.51testing.com"
website.get(dgl_url)
website.maximize_window()
# 进行页面操作
# 点击进行登录操作
login_ele = website.find_element_by_xpath("//a[@class='fl wd_fff fs12 pointer']")
login_ele.click()
tel_ele = website.find_element_by_name("name")
tel_ele.send_keys("12000000004")
pwd_ele = website.find_element_by_name("password")
pwd_ele.send_keys("111111")
com_ele = website.find_element_by_xpath("//button[@class='login_btn userLogin01']")
com_ele.click()
# 货源市场点击发布货源信息



"""
sea=website.find_element_by_id("scbar_txt")
sea.send_keys("jemter")
sub=website.find_element_by_id("scbar_btn")


sub.click()



time.sleep(3)
website.close()
time.sleep(1)
website.quit()
"""



