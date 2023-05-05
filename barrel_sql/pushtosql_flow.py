#!/usr/bin/env python
# coding: utf-8

import sqlite3
from google.cloud import storage
import pandas as pd 
import numpy as np
from datetime import datetime
import mysql.connector 
from serial import SerialException
import time
import csv
import os
import datetime as datetime
import serial.tools.list_ports
import re




def replace_string_with_zero(value):
    if isinstance(value, str):
        return 0
    else:
        return value

def replace_negative_with_zero(value):
    if value < 0:
        return abs(0)
    else:
        return value







data_gas = pd.DataFrame()
data_tank = pd.DataFrame()
upload_file_list = ['barrel_sql/Sensor_A.csv','barrel_sql/Sensor_B.csv', 'barrel_sql/Sensor_C.csv','barrel_sql/Sensor_D.csv',]

colnames = ['datetime','vals']
for upload_file in upload_file_list:
    df = pd.read_csv(upload_file,index_col=0, skiprows=0, names = colnames)
    df = df['vals'].str.split(',', expand=True)
    df.index = pd.to_datetime(df.index, format="%a %b %d %X %Y")

    if len(df.columns) > 4:
        

        df = df.iloc[:, : 5]
        data_gas = data_gas.append(df)
        
        

    
    
data_gas = data_gas.drop(columns=data_gas.columns[0])
data_gas.columns =['ID','Temp1','Temp2','Cnt']




data_gas = data_gas.sort_values(by='ID')









data_gas = data_gas[data_gas['ID'].isin(['1', '2', '3', '4'])]
data_gas.reset_index(inplace=True)
data_gas.set_index(['datetime', 'ID'], inplace=True)
data_gas = data_gas.applymap(replace_string_with_zero)
data_gas = data_gas.applymap(replace_negative_with_zero)
data_gas = data_gas.groupby(level='ID').resample('30T', level=0).max()





data_gas.reset_index(inplace=True)
data_gas['datetime'] = data_gas['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')




print(data_gas)





cnx = mysql.connector.connect(user='root', password='wase2022', host='34.89.81.147', database='Barrels_datasets')


 

cursor = cnx.cursor()
cols = "`,`".join([str(i) for i in data_gas.columns.tolist()])
for i,row in data_gas.iterrows():
    sql = "INSERT INTO `flowmeter_temperature` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))
    cnx.commit()

# os.remove(r'/home/wase-cabinet/wase-cabinet/flowmeter_push.csv')


cnx.close()

print('pushed')

# os.remove('Sensor_A.csv')
# os.remove('ensor_B.csv')
# os.remove('Sensor_C.csv')
# os.remove('Sensor_D.csv')


