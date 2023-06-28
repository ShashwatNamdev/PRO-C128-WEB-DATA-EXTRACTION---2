from bs4 import BeautifulSoup 
import requests
import pandas as pd
from selenium import webdriver
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Edge("D:\Shashwat Namdev\PRO-C127-Project-Boilerplate-main\msedgedriver.exe")
browser = requests.get(START_URL)

soup = BeautifulSoup(browser.text, "html.parser")

star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)
print(total_table)
temp_list= []

table_rows = star_table[2].find_all('tr')

for tr_tags in table_rows:
    td_tags = tr_tags.find_all('td')
    rows = [i.text.rstrip() for i in td_tags]
    temp_list.append(rows)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

headers = ['Star Name', 'Distance','Mass','Radius']
star_df_1 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=headers)

print(star_df_1)
star_df_1.to_csv('dwarf_stars.csv',index=True,index_label='id')