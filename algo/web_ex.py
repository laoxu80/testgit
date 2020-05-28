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

# 委托单管理
website.find_element_by_xpath("//li[@class='ng-scope menuL']/a[@class='inactive']/p[contains(text(),'委托单管理')]").click()
time.sleep(1)
website.find_element_by_xpath("//span[contains(text(),'委托单管理')]").click()
time.sleep(20)

# 新增委托单
#neworder_ele =WebDriverWait(website,10,1).until(EC.presence_of_element_located((By.XPATH,"//button[text()='新增委托单']")))
website.find_element_by_xpath("//*[text()='新增委托单']").click()
#neworder_ele.click()

"""
# 点击logo回到首页
website.find_element_by_xpath("//div[@class='header_logo']").click()
website.execute_script('window.scrollBy(0,500)')
time.sleep(2)
# 获取统计值
count_driver = website.find_element_by_xpath("//span[@ng-bind='searchModel.driverCount']")

count_vehicle = website.find_element_by_xpath("//span[@ng-bind='searchModel.vehicleCount']")

count_user = website.find_element_by_xpath("//span[@ng-bind='searchModel.orgCount']")

count_publish =website.find_element_by_xpath("//span[@ng-bind='searchModel.goodsSourceCount']")

count_trans = website.find_element_by_xpath("//span[@ng-bind='searchModel.weightCount']")


print("司机数：{}，车辆数：{},累计用户数：{}，发布货源数：{}，"
      "年承运吨数：{}".format(count_driver.text, count_vehicle.text,
                        count_user.text, count_publish.text, count_trans.text))


# 点击进入货源市场
pub_ele= WebDriverWait(website,5,1).until(EC.presence_of_element_located((By.LINK_TEXT,"货源市场")))
pub_ele.click()
time.sleep(1)
#website.find_element_by_link_text("货源市场").click()
# 获取统计值
total_pubnumber = website.find_element_by_xpath("//span[@ng-bind='totalModuel']")
total_pubweight = website.find_element_by_xpath("//span[@ng-bind='weightModuel']")
today_number = website.find_element_by_xpath("//span[@ng-bind='messeagModuel']")
today_weight = website.find_element_by_xpath("//span[@ng-bind='todayWeightModuel']")
print("累计货源条数：{}，累计货源吨数：{}，今日新增条数：{}，今日新增吨数：{}".format(total_pubnumber.text,
                                                       total_pubweight.text,today_number.text,today_weight.text))

website.find_element_by_xpath("//a[@class='t-btn']").click()
time.sleep(15)
# 切换到iframe1_发布货源
website.switch_to.frame("iframe1")
# 货物名称
#goods_name = WebDriverWait(website,5,1).until(EC.presence_of_element_located((By.ID,"searchModel.goodsName")))
goods_name = website.find_element_by_xpath("//input[@id='searchModel.goodsName']")

goods_name.send_keys("原油")
goods_name.click()


# 计价单位
goods_unit = website.find_element_by_id("searchModel.settlementMethod")
# 提货时间
take_time_start = website.find_element_by_id("searchModel.startTime")

take_time_start.send_keys("2020-01-01 00:00:00")
#take_time_start.click()
take_time_end = website.find_element_by_id("searchModel.endTime")

take_time_end.send_keys("2020-01-02 00:00:00")
#take_time_end.click()
#website.find_element_by_xpath("//div[@class='form-date-bar']/a[text()='确定']").click()

# 提货地址选择
take_add_ele = website.find_element_by_xpath("//span[@ng-click='addAddress1()']")
take_add_ele.click()

#website.switch_to.frame("/html/waybill/modifyAddress?__showUrl=true")





















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



