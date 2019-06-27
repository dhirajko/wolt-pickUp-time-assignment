import os
import pandas as pd
import numpy as np
import  re
current_working_directory = os.getcwd()

#validation of date
def is_date_valid(date):
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    match_iso8601 = re.compile(regex).match
    try:
        if match_iso8601(date) is not None:
            return True
    except:
        pass
    return False


#validation of integer
def is_int_valid(input):
    try:
       if(int(input)):
           return True
    except ValueError:
       return False


# calculating the date falls in given range or not
def date_fall_in_between(starting_date, ending_date, comparing_date):
    if ((starting_date < comparing_date) and (comparing_date < ending_date)):
        return True
    return False


# reading csv and returning data in array form
def reading_csv_file(location):
    df = pd.read_csv(location, sep=',', header=None, skiprows=[0])
    return df.values


# calculating median of the valid data that falls in given condition
def median_calculator(location_id, start_time, end_time):
    all_pickup_data = reading_csv_file(current_working_directory+"/median_calculator/assets/pickup_times.csv")
    selected_pickup = []
    for each_pickup in all_pickup_data:
        if ((each_pickup[0] == int(location_id)) and date_fall_in_between(start_time, end_time, each_pickup[1])):
            selected_pickup.append(each_pickup[2])
    median = np.median(np.array(selected_pickup))
    return median

