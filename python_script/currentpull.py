from traceback import print_tb
import pandas as pd
import csv
import os
import serial
from pathlib import Path
import time

import re
import subprocess

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  


#current pull with cleaning, removes datatime information at top of file and renames the file

while(1):
    
    print('--')
    try:
        path2csv = Path("/media/waselab2/B035-AD85/NGP")
        csvlist = path2csv.glob("*.csv")
        # csv = csvlist[0]
        # df = pd.read_csv(csv)
        print(csvlist)



        # colnames = ["Timestamp","U1[V]","I1[A]","P1[W]","U2[V]","I2[A]","P2[W]","U3[V]","I3[A]","P3[W]","U4[V]","I4[A]","P4[W]"]
        # data = pd.DataFrame()
        # i = 0 
        # for csv in csvlist:
        #     if i == 0:
        #         print(csv)
        #         df = pd.read_csv(csv)
        #         ls.append(df)
        #         # os.remove(csv)
        #         i += 1
        #         name = csv


    #     print(df)
    #     df.to_csv(csv)



    #     upload_online = [uploadfile1]
    #     for file in upload_online:
    #         print('uploading')
    #         gfile = drive.CreateFile({'parents': [{'id': '15m_EWk_HQalKw_CTmJsJZdgMkLMntDj6'}]})
    #         gfile.SetContentFile(file)
    #         gfile.Upload() # Upload the file.
    #         os.remove(file)
        
    #     time.sleep(5)
        
    except ValueError:
        pass
                        


