from operator import itemgetter
from time import sleep

from django.shortcuts import render

from web_app.models import JsonData
from ..DataRequest import getData
from django.db import models


# 更新表格内容
def insertAll(resquest):
    # 创建一个对象
    list_data = getData.getDataList()['line_data']
    TotalRowCount = getData.getDataList()['TotalRowCount']
    #  清空表中数据
    # JsonData.objects.all().delete()
    for i in range(0, int(TotalRowCount)):
        JsonData.objects.create(
            CODE=list_data[i]['CODE'],
            NAME=list_data[i]['NAME'],
            ADDRESS=list_data[i]['ADDRESS'],
            DES=list_data[i]['DES'],
            TIME=list_data[i]['TIME'],
            GRADE=list_data[i]['GRADE'],
            T_TIME=list_data[i]['T_TIME'],
            MAX_NUM=list_data[i]['MAX_NUM'],
            SSD=list_data[i]['SSD'],
            NUM=list_data[i]['NUM'],
            TYPE=list_data[i]['TYPE'],
            T_CODE=list_data[i]['T_CODE'],
        )


def returnAllData(request):
    #  获取数据库中最新的数据，即fetch后的数据
    #  MAX_NUM前面加上-表示按照MAX_NUM反项排序，order_by('-MAX_NUM', 'CODE')意思是，当MAX_NUM一样时按照CODE排序
    TotalRowCount = int(getData.getDataList()['TotalRowCount'])
    list_data_all = JsonData.objects.order_by('-INSERT_TIME', 'CODE')
    list_data = list_data_all[0:TotalRowCount]
    new_list = [sorted(list(list_data.values()), key=itemgetter('NUM'), reverse=True), len(list_data_all), TotalRowCount]
    return new_list


def returnDataByName(request, name):
    list_name = JsonData.objects.filter(NAME=name)
    new_list = sorted(list(list_name.values()), key=itemgetter('INSERT_TIME'), reverse=False)
    # if (len(new_list) >= 6):
    #     new_list = new_list[-6:]
    return new_list


def return_num_and_time(name, request):
    time = []
    num = []
    data = returnDataByName(request, name)
    for i in data:
        time.append(
            i['INSERT_TIME'].strftime("%Y-%m-%d %H:%M"))  # strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数 format 决定
        num.append(i['NUM'])
    data = {'time': time, 'num': num}
    return data
