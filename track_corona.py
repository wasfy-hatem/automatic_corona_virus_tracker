
import jsonpickle
#import json
import simplejson as json

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.chrome import service

import wget
##############################
import csv
from datetime import date
import time
import datetime

from pyvirtualdisplay import Display
from selenium import webdriver
import os
import sys

def get_info_for_country(site_url, site_search_box_xpath, country):

 #site_url = "https://www.hackerearth.com/problems/"
 #driver = webdriver.Opera(executable_path='/home/wasfy/python_progs/crawl_jobs/operadriver_linux64/operadriver')
 # os.getcwd()
 # os.path.join(__location__, 'operadriver')
 #driver = webdriver.Opera(executable_path='/home/wasfy/python_progs/crawl_jobs/opera_driver_2020/operadriver_linux64/operadriver')
 # wc_dir = os.path.dirname(os.path.abspath("__file__"))
 driver = webdriver.Opera(executable_path=os.path.join(os.path.dirname(os.path.abspath("__file__")), 'operadriver'))


 driver.get(site_url)

 #find all form input fields via form name
 #_inputs = driver.find_elements_by_xpath(site_form_xpath)

 driver.find_element_by_xpath(site_search_box_xpath).send_keys(country)
 time.sleep(1)  # wait for 1 seconds                               
 #####driver.refresh() #refresh the webpage 
 
 country_name_result_xpath           = "//td[1]"
 total_cases_result_xpath            = "//td[@class='sorting_1']"
 new_cases_xpath                     = "//td[3]"
 total_deaths_xpath                  = "//td[4]"
 new_deaths_xpath                    = "//td[5]"
 total_recovered_xpath               = "//td[6]"
 serious_critical_xpath              = "//td[7]"

 #driver.find_element_by_xpath(results_count_text_xpath).text
 ###print("+ -----> getting parameters")
 country_name                        = driver.find_element_by_xpath(country_name_result_xpath).text
 total_cases                         = driver.find_element_by_xpath(total_cases_result_xpath).text 
 new_cases                           = driver.find_element_by_xpath(new_cases_xpath).text 
 total_deaths                        = driver.find_element_by_xpath(total_deaths_xpath).text 
 new_deaths                          = driver.find_element_by_xpath(new_deaths_xpath).text 
 total_recovered                     = driver.find_element_by_xpath(total_recovered_xpath).text 
 serious_critical                    = driver.find_element_by_xpath(serious_critical_xpath).text 



 titles_keys      = ["country_name", "total_cases", "new_cases", "total_deaths", "new_deaths", "total_recovered", "serious_critical"]
 titles_values    = [country_name, total_cases, new_cases, total_deaths, new_deaths, total_recovered, serious_critical]
 titles_dictionary = dict(zip(titles_keys, titles_values))

 
 

 '''
 for input in _inputs:                                                             
     #print attribute name of each input element 
     print(input.get_attribute('name'))

 '''
 #driver.close() #->closing
 #driver.quit()
 return titles_dictionary, titles_keys, titles_values, driver


#----------- main Main


#site_url = https://www.hokurikugas.co.jp/inquiry2/index.asp
site_url                          = "https://www.worldometers.info/coronavirus/#countries"
site_search_box_xpath             = "//input[@class='form-control input-sm']" #
country                           = "japan"
output_html_file_path             = "/var/www/html/corona_virus_tracker.html"

display = Display(visible=0, size=(800, 600))
display.start()


titles_dictionary, titles_keys, titles_values, driver = get_info_for_country(site_url, site_search_box_xpath, country)

scrap_date = datetime.datetime.now()

print("+ Tracking script started. run time instance of: ", scrap_date)

# redirecting print to file
sys.stdout=open(output_html_file_path,"w")


print("<b>")
print("<br>")
print("_______________________________________________________________") 
print("<br>") 
print("source                 : www.worldometers.info")
print("<br>") 
print("Last tracking date     : ", scrap_date)
print("<br>") 
print("Updater                : Corona Virus Tracker v1")
print("<br>") 
print("By                     : Hatem Wasfy")
print("<br>") 
print("Contact                : ha_wasfy@yahoo.com")
print("<br>") 
print("_______________________________________________________________") 
print("<br>") 
print("|")
print("<br>") 
print("|") 
print("<br>") 

print("<br>") 
print("_______________________________________________________________")
print("<br>") 
print("Corona Virus updates for Country: ", country)
print("<br>") 
print("_______________________________________________________________")                                                               
print("<br>") 

print("<br>")
print("<br>")

indexi = 0
for title_key in titles_keys:
 #print("<br>")
 print("------------------------------------------------------------------")
 print("<br>")
 print_txt = str(title_key) + " is: " + titles_values[indexi]
 
 #print(print_txt, str(titles_keys[title_key]))
 print(print_txt)
 print("<br>")
 #print("<br>")
 indexi = indexi + 1
print("------------------------------------------------------------------")                                 
print("<br>")

sys.stdout.close()

#print("- Tracking script endeded. run time instance of: ", scrap_date)
#print("</b>")

driver.close() #->closing
driver.quit()


display.stop()

