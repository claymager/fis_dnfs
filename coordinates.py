from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chromedriver = "/run/current-system/sw/bin/cmromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

def get_coordinates( location )
    """
    Str -> IO -> Str

    returns Str formatted (Lat, Long) of a location by querying
    latlong.net
    """
    s = BeautifulSoup( input_loc(location) ) 
    return s.find("span", id_="latlngspan").text

