# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:40:15 2022

@author: HoYe110
"""

# Import Necessary Libs
from gettext import gettext
import time
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Defining headers when sending requests to a web page
my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

def weather(city):
    city = city.replace(' ', '+')
    # I. Sending requests
    my_request = requests.get(('https://www.google.com/search?q={0}-weather&oq={0}-weather&aqs=chrome..69i57j0i30l9.3375j0j7&sourceid=chrome&ie=UTF-8').format(city), headers=my_headers)


    # II. Scraping web content (html tags, css tags, content) 
    # --> mia doan nay phai hieu ve cau truc CSS HTML
    soup = BeautifulSoup(my_request.text,'html.parser')
    # Search for tags matching CSS id (id: unique across CSS tags) --> get text + strip spaces at beginning & ending --> get info: location, date, temperature, weather prediction
    location = soup.select('#wob_loc')[0].get_text().strip()
    date =  soup.select('#wob_dts')[0].get_text().strip()
    temperature = soup.select('#wob_tm')[0].get_text().strip()
    prediction = soup.select('#wob_dcp')[0].get_text().strip()
    noti = '{}\n{}\n{} °C\n{}\n'.format(
        location, date, temperature, prediction)
    
    # III. Create noti pop-up
    toaster = ToastNotifier() #initiating toaster
    toaster.show_toast('Weather Notification', noti, icon_path='weather icon.ico', duration=5, threaded=True)

weather('Ha Noi')









