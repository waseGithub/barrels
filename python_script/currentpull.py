import pandas as pd
import csv
import os
import serial
from pathlib import Path


path2csv = Path("/media/waselab2/B035-AD85")
csvlist = path2csv.glob("*.csv")


ls = []
for csv in csvlist:
    print(csv)
    ls.append(csv)
    df = pd.read_csv(csv, skiprows=14)
    print(df)





# upload_file = 
# df = pd.read_csv(upload_file,index_col=0)

