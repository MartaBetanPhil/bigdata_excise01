# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:37:50 2018

@author: lenovo
"""

###作业
print("欢迎使用天气app")
city_pinyin=input("请输入城市拼音:")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')  
data=json.loads(info)
print('今天天气是：'+data['weather'][0]['description']+',温度是：'+str(data['main']['temp'])+',气压是：'+str(data['main']['pressure']))
