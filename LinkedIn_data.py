from selenium import webdriver
import pandas as pd
import selenium.webdriver.common.keys


browser = webdriver.Chrome("C:/Users/cyber/Downloads/chromedriver_win32/chromedriver.exe")

browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
username=browser.find_element_by_id("username")
username.send_keys("*******************")
password=browser.find_element_by_id("password")
password.send_keys("********")
login_button=browser.find_element_by_class_name("login__form_action_container ")
login_button.click()

browser.get("https://www.linkedin.com/jobs")
job=browser.find_elements_by_class_name("job-card-square__title")
c=[]
for i in job:
	c.append(i.text)

job_title=[]
for i in range(len(c)):
	job_title.append(c[i].strip("Job Title\n"))
	job_title

job2=browser.find_elements_by_class_name("job-card-container__company-name")
comp_name=[]
for i in job2:
	comp_name.append(i.text)

job3=browser.find_elements_by_class_name("job-card-container__metadata-wrapper")
loc_name=[]
for i in job3:
	loc_name.append(i.text)

col=["Company Name","job title","Location"]
df=pd.DataFrame({"Company Name":comp_name[slice(10)],"job title":job_title[slice(10)],"Location":loc_name[slice(10)]})
print(df)
df.head()

