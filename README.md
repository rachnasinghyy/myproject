# myproject
this is my first respository
LinkedIn Data Scraper
This scraper will extract publicly available data:
1) I created a small program that extracts data from linkedIn and creates a  list of 10 well known companies in India.
2) Scrape data from linkedin using python and web scraping tool & libraries.
3) Extract information like Company Profile:  company name, title, location
Getting started
In order to scrape LinkedIn data, you need to make sure the scraper is logged-in into LinkedIn. when using the scraper.
1.	Create a new account on LinkedIn, or use one you already have
2.	Login to that account using your browser
3.	Open your browser's Dev Tools to find the cookie with the name.
Libraries used for Web Scraping 
As we know, Python is has various applications and there are different libraries for different purposes. In our further demonstration, we will be using the following libraries:
Selenium:  Selenium is a web testing library. It is used to automate browser activities
Pandas:  pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
Web Scraping Example : Scraping linkedin Website
Pre-requisites:
•	Python 3.x with Selenium, pandas libraries installed
•	Google-chrome browser
Step 1: Find the URL that you want to scrape
For this example, we are going scrape linkedin website to extract the Title, Company Name, and Location of Company. The URL for this page is https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin and  https://www.linkedin.com/jobs
Step 1: Inspecting the page
The data is usually nested in tags. So, we inspect the page to see, under which tag the data we want to scrape is nested. To inspect the page, just right click on the element and click  on “Inspect”.
 
When you click on the “Inspect” tab, you will see a “Browser Inspector Box” open.
 
Step 3: Find the data you want to extract
Let’s extract the Title, Company Name, and Location which is in the “div” tag respectively.
Step 4: Write the code
First, let’s create a Python file. To do this, open the file in sublime and type python <my file name> with .py extension.
I am going to name my file “LinkedIn_data”. Here’s the command:
python LinkedIn_data.py
Now, let’s write our code in this file. 
First, let us import all the necessary libraries:
1.	from selenium import *
2.	from selenium import webdriver
3.	import pandas as pd
4.	import selenium.webdriver.common.keys
To configure webdriver to use Chrome browser, we have to set the path to chromedriver
5.	browser = webdriver.Chrome("C:/Users/cyber/Downloads/chromedriver_win32/chromedriver.exe")
Refer the below code to open the URL:
6.	browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
7.	username=browser.find_element_by_id("username")
8.	username.send_keys("*******@gmail.com")
9.	password=browser.find_element_by_id("password")
10.	password.send_keys("*******")
11.	login_button=browser.find_element_by_class_name("login__form_action_container ")
12.	login_button.click()
Now that we have written the code to open the URL, it’s time to extract the data from the website. As mentioned earlier, the data we want to extract is nested in <div> tags. So, I will find the div tags with those respective class-names, extract the data and store the data in a variable. Refer the code below
13.	browser.get("https://www.linkedin.com/jobs")
14.	job=browser.find_elements_by_class_name("job-card-square__title")
15.	c=[]
16.	for i in job:
17.	#print(i.text)
18.	c.append(i.text)
19.	job_title=[]#List to store title of the company
20.	for i in range(len(c)):
21.	job_title.append(c[i].strip("Job Title\n"))
22.	job_title
23.	job2=browser.find_elements_by_class_name("job-card-container__company-name")
24.	comp_name=[]#List to store company name of the company
25.	for i in job2:
26.	#print(i.text)
27.	comp_name.append(i.text)
28.	job3=browser.find_elements_by_class_name("job-card-container__metadata-wrapper")
29.	loc_name=[]#List to store location of the company
30.	for i in job3:
31.	loc_name.append(i.text)
Step 5: Run the code and extract the data
To run the code, use the below command:
32.	python LinkedIn_data.py
Step 6: Store the data in a required format
After extracting the data, you might want to store it in a format. This format varies depending on your requirement.
33.	col=["Company Name","job title","Location"]
34.	df=pd.DataFrame({"Company Name":comp_name[slice(10)],"job title":job_title[slice(10)],"Location":loc_name[slice(10)]})
35.	print(df)
36.	df.head()
Now, I’ll run the whole code again.
 


