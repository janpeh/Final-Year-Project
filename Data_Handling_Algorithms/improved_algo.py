from datetime import datetime 
import os
import numpy as np
import pandas as pd

def change_to_date(row):
    row["date_time"] = datetime.strptime(str(row["date_time"][0:-7]), "%Y,%m,%d,%H,%M,%S")
    row["first_next_bus_estimated_arrival"] = datetime.strptime(str(row["first_next_bus_estimated_arrival"][0:-7]), "%Y,%m,%d,%H,%M,%S")
    return row

#True if bus is late, False if not latee
def check_late():
    df["late"] = np.where(df["date_time"] > df["first_next_bus_estimated_arrival"], True, False)

def late_by(): 

    total_number_of_rows = len(df)

    current_bus_number = df["bus_number"][0] #14  -- > 33
    initial_expected_arrival_time = df["first_next_bus_estimated_arrival"][0] #stores the first value first
    final1_expected_arrival_time = ""
    new2_expected_arrival_time = ""
    late_by_in_seconds = ""
    current_time = ""

    #New
    initial_first_next_bus_load = df['first_next_bus_load'][0]

    for index in range (0, total_number_of_rows - 1):
        if current_bus_number != df["bus_number"][index]: 
            current_bus_number = df["bus_number"][index]
            initial_expected_arrival_time = df["first_next_bus_estimated_arrival"][index] # the first initial of that bus number
            # df.set_value(index, 'Change Bus Number', str(current_bus_number))
            # df.at[index, 'Change Bus Number']=str(current_bus_number)

            #New
            initial_first_next_bus_load = df["first_next_bus_load"][index] # the first initial load of that bus number

        if df["bus_number"][index+1] == current_bus_number:
            current_time = df["date_time"][index]
            final1_expected_arrival_time = df["first_next_bus_estimated_arrival"][index]
            new2_expected_arrival_time = df["first_next_bus_estimated_arrival"][index+1]

            difference = (new2_expected_arrival_time-final1_expected_arrival_time).total_seconds()

            if difference > 420: #more than 7 minutes - bus change
                late_by_in_seconds = (current_time - initial_expected_arrival_time).total_seconds()

                if (late_by_in_seconds > 0):
                    # print(index, late_by_in_seconds)
                    # df.set_value(index, 'Late_By', late_by_in_seconds)
                    df.at[index, 'Late_By']=late_by_in_seconds

                else:
                    df.at[index, 'Late_By']=0
                    
                initial_expected_arrival_time = new2_expected_arrival_time

                #New
                initial_first_next_bus_load = df["first_next_bus_load"][index]
                df.at[index, 'Final Load']=initial_first_next_bus_load


def create_hour_col():
    df["Hour"] = pd.DatetimeIndex(df['date_time']).hour

srcPath = "C:/algo/dirty/" 
desPath = "C:/algo/cleaned/"

for fileName in os.listdir(srcPath):
    filePath = srcPath + fileName

    df = pd.read_csv(filePath)
    df = df.apply(change_to_date, axis="columns") # temporarily changes the date_time and first_next_bus_estimated_arrival into datetime format
    late_by()
    create_hour_col()

    print(f"Exporting {fileName}")
    df.to_csv(desPath + fileName, index=False)