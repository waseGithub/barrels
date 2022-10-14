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


path2csv = Path("/media/waselab2/B035-AD85")
csvlist = path2csv.glob("*.csv")


ls = []
colnames = ["Timestamp","U1[V]","I1[A]","P1[W]","U2[V]","I2[A]","P2[W]","U3[V]","I3[A]","P3[W]","U4[V]","I4[A]","P4[W]"]
data = pd.DataFrame()
for csv in csvlist:
    print(csv)
    df = pd.read_csv(csv, skiprows=15)
    ls.append(df)

    

curr = time.time()
curr = time.ctime(curr) 
uploadfile1 = 'power_supply_all_' + str(curr) + '.csv'
data.to_csv(uploadfile1)

df = pd.concat(ls, axis=0)
print(df)



# upload_file = 
# df = pd.read_csv(upload_file,index_col=0)

