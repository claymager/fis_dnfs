def get_season(datetime):
    season = datetime.year
    if datetime.month > 7:
        season += 1
    return season

def get_day_of_season(datetime, first_days):
    season = get_season(datetime)
    delta = datetime - first_days[season]
    return delta.days

def standardize_location(location):
    if "Beaver Creek" in location:
        return "Beaver Creek (USA)"
    elif "Aspen" in location:
        return "Aspen (USA)"
    elif "Altenmarkt" in location:
        return "Altenmarkt-Zauchensee (AUT)"
    elif "Garmisch" in location:
        return "Garmish-Partenkirchen (GER)"
    elif "Gardena" in location:
        return "Val Gardena-Groeden (ITA)"
    elif "Isere" in location:
        return "Val d'Isere (FRA)"
    elif "Zagreb" in location:
        return "Zagreb-Sljeme (CRO)"
    elif "Cortina" in location:
        return "Cortina d'Ampezzo (ITA)"
    elif "Crans" in location:
        return "Crans-Montana (SUI)"
    elif "Caterina" in location:
        return "Santa Caterina (ITA)"
    return location

def get_region(location):
    country = get_country(location)
    if country in ["AUT","CRO","SLO"]:
        region = "SE_ALPS"
    elif country in ["FIN","SVK","JPN","SUI","USA","SWE","RUS","CZE"]:
        region = "NEUTRAL"
    else:
        region = country
    return region

def get_country(location):
    return location.split(" ")[-1].replace("(","").replace(")","")

def is_olympics(record):
    month = record["datetime"].month
    year = record["datetime"].year
    country = get_country(record["location"])
    olympics = {(2018, 2,"KOR"),
                (2014, 2,"RUS"),
                (2010, 2,"CAN")}
    return (year, month, country) in olympics
