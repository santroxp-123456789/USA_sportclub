#!/usr/bin/env python
# coding: utf-8

# In[18]:


pip install selenium


# In[11]:


from selenium import webdriver #importing webdriver from selenium to scrape data from website
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

#website to be scrapped
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
#Location of downloaded chrome driver
path = 'D:/Arden University/chromedriver_win32/chromedriver.exe' 
driver = webdriver.Chrome(path)# define 'driver' variable
driver.get(website) #opens the website

# locate a button
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click() # click on a button

# select dropdown and select element inside by visible text
dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('USA')
time.sleep(3)

# select elements in the table
matches= driver.find_elements_by_tag_name('tr')

date=[]
home_team=[]
score=[]
away_team=[]

#for loop for stroing data in data frame
for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

driver.quit() #quit drive we opened in the beginning


#Create Dataframe in Pandas and export to CSV (Excel)
df= pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv(r'D:/Arden University/data1.csv')
print(df)


# In[ ]:





# In[ ]:





# In[ ]:




