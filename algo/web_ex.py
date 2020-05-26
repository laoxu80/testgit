from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
tel_ele.send_keys("11000000004")
pwd_ele = website.find_element_by_name("password")
pwd_ele.send_keys("111111")
com_ele = website.find_element_by_xpath("//button[@class='login_btn userLogin01']")
com_ele.click()
time.sleep(2)
# 验证登录用户正确
#username = website.find_element_by_id("userName")
"""
# 货源市场点击发布货源信息
website.find_element_by_xpath("//li[@class='ng-scope menuL']/a[@class='inactive']/p[contains(text(),'货源市场')]").click()
time.sleep(2)
#website.find_element_by_xpath("//a[@class='ru-a menu-a']/p[text()='货源发布']").click()
#website.find_element_by_xpath("//img[@src='../static/images/hyfb.png']").click()

pub_ele = website.find_element_by_xpath("//a[@class='menu_son_act']")
print(pub_ele)
"""
# 委托单管理
website.find_element_by_xpath("//li[@class='ng-scope menuL']/a[@class='inactive']/p[contains(text(),'委托单管理')]").click()
time.sleep(1)
website.find_element_by_xpath("//span[contains(text(),'委托单管理')]").click()
time.sleep(20)

# 新增委托单
#neworder_ele =WebDriverWait(website,10,1).until(EC.presence_of_element_located((By.XPATH,"//button[text()='新增委托单']")))
website.find_element_by_xpath("//div[@class='fl clearfix mt8 pl10']/button[text()='新增委托单']").click()
#neworder_ele.click()











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



