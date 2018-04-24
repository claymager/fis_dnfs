#!/bin/python3

from bs4 import BeautifulSoup
import re
import time

def time_to_seconds(time_str):
    """
    Str -> Float
    Converts a string formatted "%H:%m:%s."
    Returns a float measuring seconds
    """
    time = time_str.split(":")
    time = list(map(float, time))
    time = time[::-1]
    for i, t in enumerate(time):
        time[i] = t * 60 ** i
    t = sum(time)
    return t

def get_location(soup): 
    """
    Soup -> Str
    returns location of ski race
    example string: "Ofterschwang (GER)
    """
    return soup.find("div", class_="row infos").find("h2").text

def get_date(soup):
    """
    Soup -> Str
    """
    return soup.find("div", class_="large-3 columns").text.strip()

def get_racetype(soup):
    """
    Soup -> (Bool, Str)
    """
    racetype = soup.find("div", class_="racetype").find("h3").text.strip()
    # added for 18 March 2016 event handling
    # should be elsewhere
    if racetype == "Team":
        return True, "Team"
    is_ladies = "Ladies" in racetype  
    event = racetype[1+racetype.index(" "):]
    return (is_ladies, event)

def get_finish_times(soup):
    """
    Soup -> [Float]
    Returns a [Float] for number of seconds for the total time of racers who
    finished both runs
    """
    finish_times = []
    finishes = soup.find("div", class_="results").find_all("td", class_="text-left")
    for racer in finishes:
        try:
            time_str = racer.findNextSibling().text
            if len(time_str.split("."))==3:
                delim_index = time_str.find(".")
                time_str = time_str[:delim_index]+":"+time_str[delim_index+1:]
        except AttributeError:
            break # 
        finish_times.append(time_to_seconds(time_str))
    return finish_times

def get_dnfs( soup , i ):
    """
    Soup -> [Str]
    Returns a list of racers who DNF'd on race i
    """
    dnfs = []
    for elem in soup(text=re.compile(r'Did not finish '+repr(i))):
        temp = elem.parent.findNextSibling().find_all("td", class_="text-left")
        for racer in temp:
            dnfs.append(racer.text.strip())
    return dnfs

# getFisResults :: FisRaceResults -> FisEvent
def get_FIS_Results( soup ):
    """
    Soup -> ( Float, Str, Bool, Str, Str, [Float] )
    OR   -> String

    takes a soup of fis-ski format
    returns a complex tuple
        or a string describing why it failed
    """
    is_ladies, event = get_racetype( soup )
    if "Cancelled" in event:
        return "Cancelled"
    for word in ["Alpine","Team","Event","Parallel","Training"]:
        if word in event:
            return "Untracked alpine competition"

    location = get_location( soup )
    date = get_date( soup )
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
