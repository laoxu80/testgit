from selenium import webdriver


class DataCatch:

    def job_url(self,url):
        lg_web = webdriver.Chrome()
        #url = "https://www.lagou.com/shanghai/"
        lg_web.get(url)
        lg_web.maximize_window()
        # 输入“测试”点击搜索
        lg_web.find_element_by_id("search_input").send_keys("测试")
        lg_web.find_element_by_id("search_button").click()
        # 关闭“弹窗”
        lg_web.find_element_by_xpath("//div[text()='给也不要']").click()
        js1 = "window.scrollTo(0,500)"
        lg_web.execute_script(js1)
        jobeles = lg_web.find_elements_by_xpath("//a[@class='position_link']")
        jobslist = []
        for job in jobeles:
            job_url = job.get_attribute('href')
            jobslist.append(job_url)
        return jobslist


if __name__=="__main__":
    data= DataCatch()
    lagou_detail = data.job_url("https://www.lagou.com/shanghai/")
    print(lagou_detail)






