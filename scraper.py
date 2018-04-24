#!/bin/python3

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.common.exceptions import ElementNotVisibleException
import os
import time

from fis_parser import get_FIS_Results

first_url = "http://www.fis-ski.com/alpine-skiing/events-and-places/results/?season=2018&discipline=&gender=&race_id=91021&sector=AL"
os.environ["webdriver.chrome.driver"] = "chromedriver"
driver = webdriver.Chrome("chromedriver")
driver.get(first_url)

def read_visible_races():
    """
    returns list of tuples of data, for each race which can be accessed from the
    current view of the driver
    """
    output = []
    record_element = driver.find_elements_by_class_name("date-race")
    for record in record_element:
        try:
            record.click()
            time.sleep(1)
            race_results = get_results_from_driver()
            if type(race_results) == tuple:
                output.append(race_results)
        except ElementNotVisibleException:
            continue
    return output

def get_results_from_driver():
    html = driver.page_source
    soup = BeautifulSoup(html,"lxml")
    data = get_FIS_Results(soup)
    return data

#def open_months():
#    for month in driver.find_elements_by_class_name("month-label")[1:]:
#        month.click()
#    for div in driver.find_elements_by_class_name("date-more"):
#        div.click()
#
#def read_month():pass
    

#def get_year_of_races():
#    """TO VERIFY"""
#    first_url = ""
#    driver.get(first_url)
#    open_months()
#    def to_dict(rate,loc,female,event,date,finishes):
#        return ((date,loc,female,event),(rate,finishes))
#    events = dict() 
#    for event in driver.find_elements_by_class_name("date-race"):
#        key, vals = to_dict( *get_FIS_Results( event ))
#        event[key] = vals
