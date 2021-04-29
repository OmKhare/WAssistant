from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

def log_now(msg, name):
    with open("mylogs.txt", "a") as f:
        f.write(f"{name} {msg} {datetime.now()} \n")

def index(request):
 return render(request, 'index.html')

def result(request):
 name = request.GET['name']
 mins = int(request.GET['time'])
 chrome = webdriver.Chrome(ChromeDriverManager().install())
 chrome.get("https://web.whatsapp.com")
 time.sleep(10)
 search_box = chrome.find_element_by_xpath(
     "//*[@id=\"side\"]/div[1]/div/label/div/div[2]")
 search_box.send_keys(name)
 time.sleep(2)
 search_box.send_keys(Keys.ENTER)
 mins *= 60
 while(mins>0):
    try:
        online = chrome.find_element_by_xpath(
            '//*[@id="main"]/header/div[2]/div[2]')
        log_now("Online at :", name)
        time.sleep(10)
        mins -= 10
    except Exception as e:
        log_now("Offline at :", name)
        time.sleep(10)
        mins -= 10

 return render(request, 'result.html', {"result":name})

def analysis(request):
 f = open("mylogs.txt", "r")
 f1 = f.readlines()
 return render(request, 'analysis.html', {"analysis":f1})