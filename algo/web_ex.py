from selenium import webdriver
import time


website = webdriver.Chrome()
dgl_url= "https://www.daguanlian.com"
test_url = "http://bbs.51testing.com"
website.get(test_url)

sea=website.find_element_by_id("scbar_txt")
sea.send_keys("jemter")
sub=website.find_element_by_id("scbar_btn")
sub.click()




time.sleep(3)
website.close()
time.sleep(1)
website.quit()
