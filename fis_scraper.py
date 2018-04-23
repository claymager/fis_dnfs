#!/bin/python3

import requests
from bs4 import BeautifulSoup
import numpy as np
import re

def time_to_seconds(time_str):
    time = time_str.split(":")
    time = list(map(float, time))
    time = time[::-1]
    for i, t in enumerate(time):
        time[i] = t * 60 ** i
    t = sum(time)
    return t

def get_location(soup): 
    return soup.find("div", class_="row infos").find("h2").text

def get_date(soup):
    return soup.find("div", class_="large-3 columns").text.strip()

def get_racetype(soup):
    racetype = soup.find("div", class_="racetype").find("h3").text.strip()
    is_ladies = "Ladies" in racetype  
    event = racetype[1+racetype.index(" "):]
    return (is_ladies, event)

def get_finish_times(soup):
    finish_times = []
    finishes = soup.find("div", class_="results").find_all("td", class_="text-left")
    for racer in finishes:
        try:
            time_str = racer.findNextSibling().text
        except AttributeError:
            break # 
        finish_times.append(time_to_seconds(time_str))
    return finish_times

def get_dnfs( soup , i ):
    dnfs = []
    for elem in soup(text=re.compile(r'Did not finish '+repr(i))):
        temp = elem.parent.findNextSibling().find_all("td", class_="text-left")
        for racer in temp:
            dnfs.append(racer.text.strip())
    return dnfs

# getFisResults :: FisRaceResults -> FisEvent
def get_FIS_Results( soup ):
    location = get_location( soup )
    date = get_date( soup )
    is_ladies, event = get_racetype( soup )

    finishes = get_finish_times( soup )

    first_dnfs = get_dnfs( soup, 1)
    second_dnfs = get_dnfs( soup, 2)
    finished_runs = 2*len(finishes) + len(second_dnfs)
    dnf_runs = len(first_dnfs)+len(second_dnfs)
    finish_rate = dnf_runs / (finished_runs + dnf_runs)

    return ( finish_rate,
            location,
            is_ladies,
            event, 
            date, 
            finishes)
