'''
time:2018年9月24日 17：36
author:lightfish
爬取地址https://free-api.heweather.com/s6/weather/forecast?
和风天气api的使用
'''
import requests
import json
import pandas as pd



if __name__=='__main__':
    #f=open(r'E:/360下载/china-city-list.csv','r',encoding='utf-8')
    #df=pd.read_csv(f)
    #print(df['Unnamed: 2'])

    weather_url = 'https://free-api.heweather.com/s6/weather/forecast?'
    while 1:
        location = input('Please input where you want to know the weather:')
        param = {
            'location': location,
            #'lang': 'en',
            'key': '4915b670bf6b425b8c12c88f94d21ee4'
        }
        try:
            res=requests.get(weather_url, params=param)
            weather = json.loads(res.text)
            #print(res)
            weather_daily=weather['HeWeather6'][0]['daily_forecast']
            print('{}天气预报:'.format(location))
            for i in range(3):
                print('{}:\n\t白天:{}\n\t夜晚:{}\n\t最高气温:{}\n\t最低气温:{}\n\t降雨概率:{}'.format(weather_daily[i]['date'],weather_daily[i]['cond_txt_d'],weather_daily[i]['cond_txt_n'],weather_daily[i]['tmp_max'],weather_daily[i]['tmp_min'],weather_daily[i]['pop']))
        except Exception as e:
            print('请输入正确的地址！')
            continue