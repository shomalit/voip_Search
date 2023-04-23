#ITNOTG
import time
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variable Environment
title_list = []
# Functions Unit
def load_Page_init():
    path = 'chromedriver.exe'
    op = webdriver.ChromeOptions()
    #op.add_argument('--headless')
    op.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=path,chrome_options=op)
    driver.get('https://voipkala.ir')
    driver.maximize_window()
    time.sleep(2)
    cart_a = WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.XPATH,'/html/body/header/div[1]/div/div[2]/div[3]/div[1]')))
    time.sleep(2)
    cart_a.click()
    time.sleep(1)
    cart_a = WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="autocomplete_keyword"]')))
    time.sleep(1)
    cart_a.send_keys('نیوراک')
    cart_a.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.execute_script('window.scrollTo(0,2500)')
    time.sleep(1)
    return driver
def find_Title():
    ts = d.find_elements(By.CLASS_NAME,'productTitle')
    ts_n =len(ts)
    cnt = 0
    if ts_n > 0 :
        for item in ts :
            t=item.get_attribute('innerHTML')
            title_list.append(t)
            cnt +=1
            if cnt == 5 : break
    else :
        print('Not title found')
def print_Lists():
    print(title_list,end='  ')        
# Main block
d = load_Page_init()
find_Title()

print_Lists()