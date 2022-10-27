from selenium import webdriver

from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time

import pandas as pd

Start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser  = webdriver.Chrome("D:/python/PRO-C127-Reference-Code-main/chromedriver.exe")
browser.get(Start_url)

time.sleep(10)
planets_data = []
def Scrape():
    for i in range(0,5):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            
            li_tag = ul_tag.find_all("li")
            
            temp_list = []
            
            for index,li in enumerate(li_tag):
                
                if index ==0:
                    temp_list.append(li.find_all("a")[0].contents[0])
                    
                else:
                    try:
                        temp_list.append(li.contents[0])
                    except:
                        temp_list.append("")
                        
            planets_data.append(temp_list)
            
            
        browser.find_element(by=By.XPATH,value = '//*[@id="primary_column" ]/footer/div/div/div/nav/span[2]/a').click()
        
        
Scrape()

headings = ['name','light_years','mass','magnitude','date']

planets_dataset = pd.DataFrame(planets_data,columns=headings)

planets_dataset.to_csv('exoplanets.csv',index = 'True',index_label='id')
