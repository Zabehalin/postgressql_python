from lib.settings import *
import psycopg2 
import requests


db = psycopg2.connect(database="covid___19", user = user, password = passwd, host = host)
cursor = db.cursor()


def zap(url):
        #db_object.dell_corona()
        for item in url["Countries"]:
            Country = item["Country"]
            CountryCode = item["CountryCode"]
            Slug = item["Slug"]
            NewConfirmed = item["NewConfirmed"]
            TotalConfirmed = item["TotalConfirmed"]
            NewDeaths = item["NewDeaths"]
            TotalDeaths = item["TotalDeaths"]
            NewRecovered = item["NewRecovered"]
            TotalRecovered = item["TotalRecovered"]
            add_corona(Country, CountryCode, Slug, NewConfirmed, TotalConfirmed,
                                 NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)

def add_corona(Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered):
        print("add_corona")
        #clear_coron()
        #cursor.execute("TRUNCATE covid19_covid19")
        sql = "INSERT INTO covid19_covid19 (country, countrycode, slug, newconfirmed, totalconfirmed, newdeaths, totaldeaths, newrecovered, totalrecovered) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql = "INSERT INTO covid19_covid19 (country, countrycode, slug, newconfirmed, totalconfirmed, newdeaths, totaldeaths, newrecovered, totalrecovered) VALUES ('" + str(Country) + "', '" + str(CountryCode) + "', '" + str(Slug) + "', '" + str(NewConfirmed) + "', '" + str(TotalConfirmed) + "', '" + str(NewDeaths) + "', '" + str(TotalDeaths) + "', '" + str(NewRecovered) + "', '" + str(TotalRecovered) + "')"
        val = (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed,NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)
        cursor.execute(sql, val)
        db.commit()

def clear_coron():
        cursor.execute("TRUNCATE covid19_covid19")
        db.commit()
