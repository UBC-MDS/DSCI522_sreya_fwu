
# coding: utf-8

# In[1]:


# 01_data-clean.ipynb
# 
# TEAM: Fan Wu & Sreya Guha
# DATE: November 23, 2018
#
# PURPOSE: The script takes a raw crime dataset and generates a clean dataset through cleaning
#          null values, updating data formats, and classifying data.
#
# INPUT: 
#     - Raw Dataset: "data/crime_1617_raw_data.csv"
# 
# OUTPUT:
#     - Clean Dataset: "data/crime_1617_clean_data.csv"
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
    
    '''main function: grab the arg1 and arg2 as input file path and output file path '''
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_wrangling(input_file, output_file)
    
def drop_null(df):
    
    '''drop_null function is to drop all null values in a dataframe'''
    
    if df.isnull().values.any() == True:
        df.dropna()
    return df

def update_datatime(df, col, new_col, req):
    
    '''update_datatime function will update a Date-format column to a new column by 
       the specific requirements (i.e. date or time)'''
    
    if req == "date":
        df[new_col] = [d.date() for d in df[col]]
    elif req == "time":
        df[new_col] = [d.time() for d in df[col]]
    
def update_boolean(df, col):
    
    '''update_boolean function will update a boolean column (i.e. True/False) to 1/0'''
    
    df[[col]] *= 1


def export_clean_data(df, output_file):
    
    '''export_clean_data function is used to generate a csv file for the clean dataset'''
    
    df.to_csv(output_file, index=False)

def data_wrangling(input_file, output_file):
    
    '''data_wrangling function takes two arguments (i.e. input_file path and output_file path),
       and generate a clean dataset'''
    
    #import raw dataset
    crime_data = pd.read_csv(input_file)
    crime_clean_data = crime_data.dropna()
    crime_clean_data.Date = pd.to_datetime(crime_clean_data.Date)
    
    #update data types for `Date`, `Arrest`, and `Domestic`
    update_datatime(crime_clean_data, 'Date', 'Crime_Date', 'date')
    update_datatime(crime_clean_data, 'Date', 'Crime_Time', 'time')
    for col in ['Arrest', 'Domestic']:
        update_boolean(crime_clean_data, col)
    
    #data classification for the `Primary.Type`
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
    
    #export the clean dataset to output file path
    export_clean_data(crime_clean_data, output_file)

#call main function
if __name__ == '__main__':
    main()

