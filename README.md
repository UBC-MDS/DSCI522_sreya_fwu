# A Crime Data Analysis in Chicago

| **Team Members** |
| -- |
| Fan Wu |
| Sreya Guha |


### Chicago Crimes Dataset
We are going to analyze the Chicago crimes dataset that reflects the crimes occurred in Chicago from 2016-2017. The dataset includes the following contents:

| Column name | datatype | Description |
| --- | -- | -- |
| ID | Numeric | Identifier for a particular case of crime |
| Case Number | String | Case number with the police | 
| Date | Date | Date and time at which the crime occured | 
| Block | String | Block where the crime occured | 
| IUCR | Numeric | Illinois Uniform Crime Reporting |
| Primary Type | String | Type of crime |
| Description | String | Description of the crime |
| Location Description | String | Location of the crime |
| Arrest | Boolean | Whether an arrest was made | 
| Domestic | Boolean | Whether it is a domestic violence case | 
| Beat | Numeric | -- | 
| District | Numeric | Disrict where the crime occured | 
| Ward | Numeric | Ward where the crime occured | 
| Community Area | Numeric | Community area where the crime occured |
| FBI Code | Numeric | FBI code for the crime |
| X Coordinate | Numeric | Loaction co-ordinates of the crime |
| Y Coordinate | Numeric | Loaction co-ordinates of the crime |
| Year | Numeric | Year when the crime occured | 
| Updated On | Date | Time and date when the investigation for the crime was updated | 
| Latitude | Numeric | Loaction co-ordinates of the crime | 
| Longitude | Numeric | Loaction co-ordinates of the crime |
| Location | String | Location of the crime |


We write a script to download the dataset as follow:

![image](https://github.com/UBC-MDS/DSCI522_sreya_fwu/blob/master/img/screenshot_data_load.png)


### Predictive Question

**What are the strongest predictors of an arrest result for a crime in Chicago?**

### Data Analysis Plan

The goal of this analysis is to explore the Chicago Crimes Dataset from 2016-2017, classify the features that determine the arrest result, and construct a prediction model to identify whether an arrest could happen for a future crime. The detailed steps for this analysis are:

Step 1. Load data into Python

Step 2. Data wrangling:

- Checking missing values
- Dealing with null values
- Cleaning the description column with standard keywords
- Putting the arrest and domestic columns into 1 (True) or 0 (False)
- Separating the date and time into two columns.

Step 3. Visualizations of the dataset:

- Which crime was maximum? 
- Location with the highest crime rate
- Crimes trend among 2016-2017
- Summary of the arrest results

Step 4. Prediction Model: 

In this analysis, we will apply the decision tree method to find the strongest features that are able to predict the arrest result.

- Separate the dataset into training and testing datasets (7:3).
- Define the variable X to be a feature vector includes the time of the crime, primary type, description, location, and domestic.
- Define the target variable Y to be the arrest result. 
- Use the decision tree package in Python (i.e. Scikit Learn) to model the relationship between X and Y. 
- Once we get the tree, we can use it to get the predicted arrest results for the testing dataset and compare them with the actual results to get the accuracy rate.


### Experimental Results

To present our result, we will draw the entire tree as we only consider five features and indicate the strongest predictors chosen by this method. Additionally, we will report the classification error.

