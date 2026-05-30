from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import sys
import time
from requests import get
from lxml import html, etree
from lxml.html.clean import clean_html

url ="http://tdil-dc.in/san/skt_gen/kqw/kqw_gen.html"
driver = webdriver.Chrome()
driver.get(url)
parentWindow = driver.current_window_handle
element = driver.find_element_by_xpath("//select[@name='vb']")
all_options = element.find_elements_by_tag_name("option")
button = driver.find_element_by_xpath("//input[@type='submit']")

f = open("ndata.txt", 'w')
sys.stdout = f

for option in all_options:
    root = "root -   "+ option.text + "\n"
    rootN = "".join(root).encode('utf-8').strip()
    f.write(rootN)
    option.click()
    button.click()
    frame1 = driver.find_element_by_xpath("//iframe[@name='showMyopt1']")
    driver.switch_to.frame(frame1)
    i = 0
    for node in driver.find_elements_by_xpath("//center[1]//tr"):
        if i > 1:
            arr1 = node.find_element_by_xpath("./td[2]/font/form/input[@type='submit']").get_attribute("value")
            arr2 = node.find_element_by_xpath("./td[3]/font/form/input[@type='submit']").get_attribute("value")
            arr3 = node.find_element_by_xpath("./td[4]/font/form/input[@type='submit']").get_attribute("value")
            data1 =  node.text+ " " + arr1 + " " + arr2 + " " + arr3 + "\n"
            newData1 = "".join(data1).encode('utf-8').strip()
            print newData1
            i+1
            continue
        i = i+1
        # newData = "".join(node.text).encode('utf-8').strip()
        # f = open("data", 'w')
        # f.write(newData)
        # f.close
    j = 0
    for node in driver.find_elements_by_xpath("//center[2]//tr"):
        if j > 0:
            data2 = node.text + "\n"
            newData2 = "".join(data2).encode('utf-8').strip()
            print newData2
            j+1
            continue
        j = j+1
    driver.switch_to.window(parentWindow)
f.close 
driver.close