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




while(1):
    
    print('--')
    # try:
    path2csv = Path("/media/waselab2/B035-AD85/NGP/logging")
    csvlist = path2csv.glob("*.csv")
    ls = []
    names = []
    # colnames = ["Timestamp","U1[V]","I1[A]","P1[W]","U2[V]","I2[A]","P2[W]","U3[V]","I3[A]","P3[W]","U4[V]","I4[A]","P4[W]"]
    data = pd.DataFrame()
    for csv in csvlist:
        
        df = pd.read_csv(csv, keep_default_na=True)
        print("reading")

        ls.append(df)
        names.append(str(csv))




    df = ls[0]
    name = names[0]
    print(df)

    curr = time.time()
    curr = time.ctime(curr) 
    uploadfile1 = name
    x = uploadfile1.split("/")
    uploadfile = x[-1]
    uploadfile = "power_data" + "-" + curr + "-" + uploadfile
    print(uploadfile)
    df.to_csv(uploadfile)



    upload_online = [uploadfile]

    
    print(x)

    for file in upload_online:
        print('uploading')
        gfile = drive.CreateFile({'parents': [{'id': '15m_EWk_HQalKw_CTmJsJZdgMkLMntDj6'}]})
        gfile.SetContentFile(file)
        gfile.Upload() # Upload the file.
        os.remove(file)
    
    time.sleep(5)
        
    # except ValueError:
    #     pass
                        

    # upload_file = 
    # df = pd.read_csv(upload_file,index_col=0)

