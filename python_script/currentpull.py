import pandas as pd
import csv
import os
import serial
import Path 


path2csv = Path("/media/waselab2/B035-AD85")
csvlist = path2csv.glob("*.csv")



for csv in csvlist:
    print(csv)
# upload_file = 
# df = pd.read_csv(upload_file,index_col=0)
