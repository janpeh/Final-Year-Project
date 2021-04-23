import datetime
from datetime import timedelta
import os
import numpy as np
import pandas as pd

def correct_datetime(): 
    df['new_datetime'] = ''
    for i in range(0,144379): 
        print(i)
        test = str(df["datetime"][i])[0:-7]
        new_datetime = datetime.datetime.strptime(test, "%Y,%m,%d,%H,%M,%S")
        df['new_datetime'][i] = new_datetime

srcPath = "C:/FYP-mine/General_data/Taxi Data Phase 2/taxi2_dirty/" 
desPath = "C:/FYP-mine/General_data/Taxi Data Phase 2/taxi2_clean/"

for fileName in os.listdir(srcPath):
    filePath = srcPath + fileName

    df = pd.read_csv(filePath)
    # df = df.apply(change_to_date, axis="columns") # temporarily changes the date_time and first_next_bus_estimated_arrival into datetime format
    correct_datetime()

    print(f"Exporting {fileName}")
    df.to_csv(desPath + fileName, index=False)