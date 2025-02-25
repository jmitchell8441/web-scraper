from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" - incognito")
chromedriver_path = 'C:/Users/jabar/Documents/chromedriver-win64/chromedriver.exe'

def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)

#Opening the website
browser = webdriver.Chrome()
browser.get("https://github.com/collections/machine-learning")
projects = browser.find_elements("xpath", "//h1[@class='h3 lh-condensed']")

project_list = {}
for proj in projects:
    proj_name = proj.text #Project name
    proj_url = proj.find_elements("xpath", "a")[0].get_attribute('href') #Project Url
    project_list[proj_name] = proj_url

browser.quit()

#Putting data into file
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

#Make table look more readable 
project_df['project_name'] = project_df.index
project_df.colums = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)

