import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from Episodio import Episodio

url = 'https://animesonline.cc/anime/tensei-shitara-slime-datta-ken/'
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)

time.sleep(10)

listElements = driver.find_elements(By.CLASS_NAME, 'episodios')
epis = []
for e in listElements:
    season = e.find_elements(By.TAG_NAME, 'li')
    for epi in season:
        number = epi.find_element(
            By.CLASS_NAME, 'episodiotitle').find_element(By.TAG_NAME, 'a').text
        img = epi.find_element(By.TAG_NAME, 'img').get_property('src')
        link = epi.find_element(By.TAG_NAME, 'a').get_property('href')

        data = {number, link, img}
        episodio = Episodio()
        episodio.number = number
        episodio.link = link
        episodio.img = img
        print(episodio.img)

# listImg = listElements.find_elements(By.TAG_NAME, 'img')
# listTitles = listElements.find_elements(
#     By.CLASS_NAME, 'episodiotitle')

# listEpi = []
# for e in listImg:
#     epi = e.get_property('src')
#     print(epi)
#
# for e in listTitles:
#     print(e.find_element(By.TAG_NAME, 'a').text)


driver.quit()
