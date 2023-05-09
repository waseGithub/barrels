#!/usr/bin/env python
# coding: utf-8

import sqlite3
from google.cloud import storage
import pandas as pd 
import numpy as np
from datetime import datetime
import mysql.connector 
import sys 
import os
import pandas as pd
from pathlib import Path






def format_rs_csv(csvdest):
    path2csv = Path(csvdest)
    csvlist = path2csv.glob("*.csv")

    for i in csvlist:
        print(i)
        csvlist = [] 
        csvlist.append(i)


    csv = csvlist[0]

    df_header = pd.read_csv(csv, nrows=14, names=['attribute', 'data'])
    colnames = ["Timestamp","U1[V]","I1[A]","P1[W]","U2[V]","I2[A]","P2[W]","U3[V]","I3[A]","P3[W]","U4[V]","I4[A]","P4[W]"]
    df = pd.read_csv(csv, skiprows=16, names=colnames)

    start_time = df_header[df_header['attribute'] == '#Start Time'].data.values[0]
    start_date = df_header[df_header['attribute'] == '#Date'].data.values[0]
    start_datetime = str(str(start_date) + " " + str(start_time))
    increment = df_header[df_header['attribute'] == '#Logging Interval[s]'].data.values[0]
    increment = int(float(increment))/ 60
    count_row = df.shape[0] 
    duration = increment * (count_row)
    end_datetime= pd.to_datetime(start_datetime) + pd.to_timedelta(duration,'m')
        # print(duration)
        # print(count_row)    
        # print("start time", start_datetime)
        # print("end time", end_datetime)

    ls_datetime_range = pd.date_range(start=start_datetime, periods=count_row, freq='5Min')
    df_datetimes = pd.DataFrame(ls_datetime_range, columns=['datetime'])
    df = pd.concat([df, df_datetimes], axis=1)
    df.set_index('datetime', inplace =True)
    df = df.tail(6)

    return df





    
def append_rs_csv_to_ls(df, tank_names_ls):

    single_tank_ls = []
    for tank in tank_names_ls:
        print(tank)
        index_value = barrels_postion.get(tank)
        print(index_value)

        single_tank_df = df[["U" + str(index_value) + "[V]", "I" + str(index_value) +"[A]", "P" + str(index_value) + "[W]"]]

        
        # single_tank_df['ID'] = tank
        single_tank_df.insert(1, "ID", tank, True)

      


        # single_tank_df.loc['ID'] = tank
        
        single_tank_df = single_tank_df.rename(columns={"U" + str(index_value) + "[V]" :'V', "I" + str(index_value) +"[A]" : 'A', "P" + str(index_value) + "[W]":'P'})
        single_tank_ls.append(single_tank_df)
    concat_df = pd.concat(single_tank_ls, axis=0)
    concat_df.reset_index(inplace=True)
    concat_df.set_index(['datetime', 'ID'], inplace=True)
    concat_df = concat_df.groupby([pd.Grouper(freq='30T', level='datetime'), pd.Grouper(level='ID')])['V', 'A', 'P'].mean()  



    return concat_df
    




power_ls = []    
# print(power_ls)



#########
#########


# psu_pathtop = '/home/farscopestudent/Documents/WASE/wase-cabinet/rohde_schwarz'
# psu_pathmid = '/home/farscopestudent/Documents/WASE/wase-cabinet/rohde_schwarz'
# psu_pathbot = '/home/farscopestudent/Documents/WASE/wase-cabinet/rohde_schwarz'

barrel_psu= 'ftp://barrelspsu@169.254.8.8/int/logging/'



df_barrels = format_rs_csv(link_ls[0])

# power supplies middle and bottom were set to timezone an hour out - this adjusts them to the current time zone
# df_bot = df_bot.shift(periods=-1, freq="60T")





df_barrels = append_rs_csv_to_ls(df_barrels, ['1', '2', '3', '4'])

df_ls = [df_barrels]
power_df = pd.concat(df_ls, axis=0) 


print(power_df)
power_df.reset_index(inplace=True)
power_df = power_df.rename(columns={"V": "voltageV", "A": "currentA", "P": "powerP", 'ID':'Name'})
print(power_df)



 




######################
######################
######################



cnx = mysql.connector.connect(user='root', password='wase2022', host='34.89.81.147', database='cabinet_datasets')


cursor = cnx.cursor()
cols = "`,`".join([str(i) for i in power_df.columns.tolist()])
for i,row in power_df.iterrows():
    sql = "INSERT INTO `rs_current_data` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))
    cnx.commit()

# Create cursor
my_cursor = cnx.cursor()


# # Execute Query
# my_cursor.execute("SELECT * from flowmeter")

# # Fetch the records
# result = my_cursor.fetchall()

# for i in result:
#     print(i)

# Close the connection
cnx.close()