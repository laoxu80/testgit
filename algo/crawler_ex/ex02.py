from selenium import webdriver
import pandas as pd



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
        lg_web.close()
        return jobslist

    def job_detail(self,urllist):
        list_job=[]
        for url in urllist:
            job_dict = {}
            detail = webdriver.Chrome()
            detail.get(url)
            detail.maximize_window()
            title = detail.find_element_by_class_name("name")
            job_dict['title'] = title.text
            salary = detail.find_element_by_class_name("salary")
            job_dict['salary'] = salary.text
            desc = detail.find_element_by_class_name("job-detail")
            job_dict['desc'] = desc.text
            address = detail.find_element_by_class_name("work_addr")
            job_dict['address'] = address.text
            company = detail.find_element_by_class_name("job_company_content")
            job_dict['comp'] = company.text
            detail.close()
            list_job.append(job_dict)
        return list_job

    def save_data(self,joblist):
        dt=pd.DataFrame(joblist)
        dt.to_excel("panda_data.xlsx",sheet_name="Sheet1")
        return None




if __name__=="__main__":
    data= DataCatch()
    lagou_detail = data.job_url("https://www.lagou.com/shanghai/")
    #DataCatch().job_url("https://www.lagou.com/shanghai/")
    print(lagou_detail)
    joblist =data.job_detail(lagou_detail)
    print(joblist)
    data.save_data(joblist)






