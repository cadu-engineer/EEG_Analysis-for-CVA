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
navegador = webdriver.Chrome(options=options)

navegador.get("https://nedc-tuh-eeg:RLYF8ZhBMZwNnsYA8FsP@isip.piconepress.com/projects/nedc/data/tuh_eeg/tuh_eeg_abnormal/v3.0.1/edf/eval/abnormal/01_tcp_ar/")

links = navegador.find_elements(By.TAG_NAME, "a")

for link in links[5:-1]:
    actions = ActionChains(navegador)
    actions.context_click(link).perform()
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
    sleep(0.3)







