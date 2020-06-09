from selenium import webdriver
job_dict ={}
detail = webdriver.Chrome()
url = "https://www.lagou.com/jobs/7264083.html?show=25f52a3dd7914782be472104b991ac24"
detail.get(url)
detail.maximize_window()
title = detail.find_element_by_class_name("name")
job_dict['title']=title.text
salary = detail.find_element_by_class_name("salary")
job_dict['salary']=salary.text
desc= detail.find_element_by_class_name("job-detail")
job_dict['desc']=desc.text
address= detail.find_element_by_class_name("work_addr")
job_dict['address']=address.text
company = detail.find_element_by_class_name("job_company_content")
job_dict['comp']=company.text
detail.quit()





print(job_dict)