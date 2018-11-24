
# coding: utf-8

# In[92]:


# 01_data-clean.ipynb

# PURPOSE: The script takes the raw crime dataset and generates the clean dataset
#
# ARGUMENTS:
#     ARG1 = input file path
#     ARG2 = output file path
#
# USAGE: "python src/01_data-clean.py data/crime_1617_raw_data.csv data/crime_1617_clean_data.csv"

import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_wrangling(input_file, output_file)
    
def drop_null(df):
    if df.isnull().values.any() == True:
        df.dropna()
    return df

def update_datatime(df, col, new_col, req):
    if req == "date":
        df[new_col] = [d.date() for d in df[col]]
    elif req == "time":
        df[new_col] = [d.time() for d in df[col]]
    
def update_boolean(df, col):
    df[[col]] *= 1


def export_clean_data(df, output_file):
    df.to_csv(output_file, index=False)

def data_wrangling(input_file, output_file):
    crime_data = pd.read_csv(input_file)
    crime_clean_data = crime_data.dropna()
    crime_clean_data.Date = pd.to_datetime(crime_clean_data.Date)
    update_datatime(crime_clean_data, 'Date', 'Crime_Date', 'date')
    update_datatime(crime_clean_data, 'Date', 'Crime_Time', 'time')
    for col in ['Arrest', 'Domestic']:
        update_boolean(crime_clean_data, col)
    #update_boolean(crime_clean_data, 'Arrest')
    #update_boolean(crime_clean_data, 'Domestic')
    crime_clean_data[['Primary.Type']] = crime_clean_data['Primary.Type'].replace(['THEFT', 'BURGLARY', 'MOTOR VEHICLE THEFT', 'ROBBERY' ,'BATTERY', 'CRIM SEXUAL ASSAULT',
                                        'SEX OFFENSE' , 'NARCOTICS','OTHER NARCOTIC VIOLATION' , 'ASSAULT', 'INTIMIDATION' ,
                                        'OTHER OFFENSE' , 'DECEPTIVE PRACTICE' , 'CRIMINAL TRESPASS' , 'WEAPONS VIOLATION' , 
                                        'CONCEALED CARRY LICENSE VIOLATION','PUBLIC INDECENCY', 'PUBLIC PEACE VIOLATION',
                                        'OFFENSE INVOLVING CHILDREN','PROSTITUTION','INTERFERENCE WITH PUBLIC OFFICER','HOMICIDE',
                                        'ARSON', 'CRIMINAL DAMAGE','GAMBLING','LIQUOR LAW VIOLATION','KIDNAPPING','STALKING', 
                                        'OBSCENITY','NON-CRIMINAL','NON-CRIMINAL', 'NON-CRIMINAL (SUBJECT SPECIFIED)','HUMAN TRAFFICKING']
                    ,['THEFT','THEFT','THEFT','THEFT','SEXUAL ASSAULT','SEXUAL ASSAULT','SEXUAL ASSAULT','NARCOTICS','NARCOTICS','ASSAULT','ASSAULT','OTHER OFFENSE','DECETIVE PRACTICE',
                      'CRIMINAL TRESPASS','WEAPONS VIOLATION','WEAPONS VIOLATION','PUBLIC INDECENCY','PUBLIC INDECENCY','OFFENSE INVOLVING CHILDREN','PROSTITUTION','INTERFERENCE WITH PUBLIC OFFICER',
                      'HOMICIDE','ARSON','ARSON','GAMBLING','LIQUOR LAW VIOLATION','KIDNAPPING','STALKING','STALKING','NON-CRIMINAL','NON-CRIMINAL','NON-CRIMINAL','HUMAN TRAFFICKING'])
    export_clean_data(crime_clean_data, output_file)

if __name__ == '__main__':
    main()

