import datetime
from datetime import timedelta
import os
import numpy as np
import pandas as pd

# CHANGE TO DATE (revised)
def change_to_date(row):
    row["datetime"] = datetime.datetime.strptime(str(row["datetime"][0:-7]), "%Y,%m,%d,%H,%M,%S")
    return row

def taxi_count():

    num_rows = len(df)
    count = 0
    index = 0

    base_datetime = df["datetime"][0]
    base_datetime = base_datetime - timedelta(minutes = 4, seconds=44)
    print('base')
    print(base_datetime)
    new_datetime = base_datetime + timedelta(hours=1)
    print('new')
    print(new_datetime)

    index < (num_rows - 1)

    while (new_datetime >= base_datetime and index < (num_rows - 1)): 
        count += 1
        index += 1
        # print(index)
        base_datetime = df["datetime"][index]
        df.at[index-1, 'new_datetime'] = new_datetime
        # print('while'  + str(base_datetime))

        if (base_datetime > new_datetime):
            df.at[index-1, 'count'] = count
            while (new_datetime < base_datetime): 
                new_datetime = new_datetime + timedelta(hours=1)
                df.at[index-1, 'new_datetime'] = new_datetime
            # print('new')
            # print(new_datetime)
            count = 0
            continue
    
    if (index == (num_rows - 1)): 
        df.at[index, 'count'] = count

srcPath = "C:/FYP/FYPDB/taxi_dirty/" 
desPath = "C:/FYP/FYPDB/taxi_clean/"

for fileName in os.listdir(srcPath):
    filePath = srcPath + fileName

    df = pd.read_csv(filePath)
    df = df.apply(change_to_date, axis="columns") # temporarily changes the date_time and first_next_bus_estimated_arrival into datetime format
    taxi_count()

    print(f"Exporting {fileName}")
    df.to_csv(desPath + fileName, index=False)