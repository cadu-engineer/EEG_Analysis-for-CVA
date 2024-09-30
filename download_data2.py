import tueg_tools
import os
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import pyautogui
options = Options()
path_folder = 'C:/Users/carlo/Desktop/EEG_Analysis/EEG_Analysis-for-CVA/Dataset/tuh_eeg_epilepsy/00_epilepsy/'
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:/Users/carlo/Desktop/EEG_Analysis/EEG_Analysis-for-CVA/Dataset/tuh_eeg_epilepsy/00_epilepsy/", "directory_upgrade": True}
chromeOptions.add_experimental_option("prefs",prefs)
navegador = webdriver.Chrome(options=chromeOptions)

navegador.get("https://nedc-tuh-eeg:RLYF8ZhBMZwNnsYA8FsP@isip.piconepress.com/projects/nedc/data/tuh_eeg/tuh_eeg_epilepsy/v2.0.1/00_epilepsy/")

links1 = navegador.find_elements(By.TAG_NAME, "a")

for link1 in links1[5:-1]:
    actions = ActionChains(navegador)
    actions.click(link1).perform()
    links2 = navegador.find_elements(By.TAG_NAME, "a")

    for link2 in links2[5:-1]:
        actions.click(link2).perform()
        links3 = navegador.find_elements(By.TAG_NAME, "a")
        for link3 in links3[5:-1]:
            actions.click(link3).perform()
            path_web = navegador.find_element(By.TAG_NAME, "h1").text
            path = path_web.split('/')
            path_folder = 'C:/Users/carlo/Desktop/EEG_Analysis/EEG_Analysis-for-CVA/Dataset/tuh_eeg_epilepsy/00_epilepsy/' + path[-3] + '/' + path[-2] + '/' + path[-1]
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)
            # prefs = {"download.default_directory" : path_folder}
            # options.add_experimental_option("prefs",prefs)
            # navegador.options = options
            
            print('folder', path_folder)
            links4 = navegador.find_elements(By.TAG_NAME, "a")
            for link4 in links4[5:-1]:
                actions.context_click(link4).perform()
                pyautogui.press("down")
                # sleep(0.3)
                pyautogui.press("down")
                # sleep(0.3)
                pyautogui.press("down")
                # sleep(0.3)
                pyautogui.press("down")
                # sleep(0.3)
                pyautogui.press("enter")
                sleep(1.2)
                pyautogui.press("enter")
                sleep(5)
                print('link:', path_web)


# import tueg_tools
# ds = tueg_tools.Dataset('C:\Downloads')
# ds.download('https://isip.piconepress.com/projects/nedc/data/tuh_eeg/tuh_eeg_epilepsy/v2.0.1/',
#              username='nedc-tuh-eeg', password='RLYF8ZhBMZwNnsYA8FsP', maxSize=10**11)

    
    
    
    
    
    
    
    
    
# pyautogui.press("down")
# # sleep(0.3)
# pyautogui.press("down")
# # sleep(0.3)
# pyautogui.press("down")
# # sleep(0.3)
# pyautogui.press("down")
# # sleep(0.3)
# pyautogui.press("enter")
# sleep(1.2)
# pyautogui.press("enter")
# sleep(0.3)







