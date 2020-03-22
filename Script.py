"""
Title: Automated Script for Data Scraping

Creator: Haris "5w464l1c10u5"

Purpose: This was made in order to make it easier to get data from online, all through one python script

Usage:
python3 Automated_Script.py

Resources:
https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
https://www.guru99.com/reading-and-writing-files-in-python.html
https://www.dataquest.io/blog/web-scraping-tutorial-python/
https://forecast.weather.gov/MapClick.php?lat=42.00900000000007&lon=-87.69495999999998
https://pythonspot.com/http-download-file-with-python/

"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
from datetime import date, datetime
import io
import codecs

Code_Version = 3
#Time in H:M:S format
now = datetime.now()
Time = now.strftime("%I:%M:%S:%p")

#Date
Today_Date = date.today()
Date = Today_Date.strftime("(%A) %B %d, %Y")

try:
    #Weather
    page = requests.get('https://forecast.weather.gov/MapClick.php?lat=42.00900000000007&lon=-87.69495999999998')
    soup = BeautifulSoup(page.text, 'html.parser')
except:
    print("Weather.gov is not available")

try:
    #Weather Type
    weathertype = soup.find(class_='myforecast-current')
    type = weathertype.contents[0]
    type = type.encode('utf-8')
except:
    type = "N/A"

try:
    #Fahrenheit
    weather = soup.find(class_='myforecast-current-lrg')
    w = weather.contents[0]
    w = w.encode('utf-8')
except:
    w = "N/A"

try:
    #Humidity
    Humidity = soup.find_all('td')[0].get_text()
    Hum_percent = soup.find_all('td')[1].get_text()
except:
    Humidity = "N/A"
    Hum_percent = "N/A"

try:
    #Wind_Speed
    W_Speed = soup.find_all('td')[2].get_text()
    W_S = soup.find_all('td')[3].get_text()
except:
    W_Speed = "N/A"
    W_S = "N/A"

try:
    #Wind_Chill
    Wind_Chill = soup.find_all('td')[10].get_text()
    Wind_Chill_num = soup.find_all('td')[11].get_text()
    Wind_Chill = Wind_Chill.encode('utf-8')
    Wind_Chill_num = Wind_Chill_num.encode('utf-8')
except:
    Wind_Chill = "N/A"
    Wind_Chill_num = "N/A"

try:
    #Last_Update
    Last_Update = soup.find_all('td')[12].get_text()
    Last_Update_num = soup.find_all('td')[13].get_text()
except:
    Last_Update = "N/A"
    Last_Update_num = "N/A"


html_file = """
<h1 style="text-align: center;"><span style="text-decoration: underline;">Good Morning, Haris!</span></h1>
<h4 style="text-align: left;">Time:</h4>
<h4 style="text-align: left;">Date:</h4>
<h4>Code Version:</h4>
<hr />
<h3 style="font-size: 1.5em; text-align: center;"><span style="text-decoration: underline;"><span style="background-color: #00ccff;">Weather</span></span></h3>
<table style="margin-left: auto; margin-right: auto; height: 195px;" width="238">
<tbody>
<tr style="height: 7px;">
<td style="width: 228px; height: 7px;">Current Weather:</td>
</tr>
<tr style="height: 1px;">
<td style="width: 228px; height: 1px;">Weather Type:</td>
</tr>
<tr style="height: 2px;">
<td style="width: 228px; height: 2px;">Humidity:</td>
</tr>
<tr style="height: 2px;">
<td style="width: 228px; height: 2px;">Wind Speed:</td>
</tr>
<tr style="height: 2px;">
<td style="width: 228px; height: 2px;">Wind Chill:</td>
</tr>
<tr style="height: 2px;">
<td style="width: 228px; height: 2px;">Last Update:</td>
</tr>
</tbody>
</table>
<p style="font-size: 1.5em;">&nbsp;</p>
<hr />
<h3 style="font-size: 1.5em; text-align: center;"><span style="text-decoration: underline; background-color: #cc99ff;">News</span></h3>
"""


html_file = html_file.replace('Time:','Current Time: ' + Time)
html_file = html_file.replace('Date:','Today\'s Date: ' + Date)
html_file = html_file.replace('Code Version:', 'Code Version: #' + str(Code_Version))

html_file = html_file.replace('Current Weather:','Current Weather: ' + w.decode('utf8'))
html_file = html_file.replace('Weather Type:','Weather Type: ' + type.decode('utf8'))
html_file = html_file.replace('Humidity:','Humidity: ' + Hum_percent)
html_file = html_file.replace('Wind Speed:','Wind Speed: ' + W_S)
html_file = html_file.replace('Wind Chill:','Wind Chill: ' + Wind_Chill_num.decode('utf-8'))

html_file = html_file.replace('Last Update:','Last Update: ' + Last_Update_num)


try:
    response = urllib.request.urlopen('https://allinfosecnews.com/')
    html = response.read()
except:
    print("https://allinfosecnews.com/ is not available")

with io.open("website.html", 'w', encoding='utf8') as f:
    f.write(html_file)
    f.write(html.decode('utf-8'))

f.close()

print(w)
print(type)
print(Hum_percent)
print(W_Speed)
print(W_S)
print(Wind_Chill_num)
print(Last_Update_num)
