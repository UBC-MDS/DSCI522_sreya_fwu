# A Crime Data Analysis in Chicago

### Team Information

|Name|GitHub UBC Personal Repo - Proposal|
|--|--|--|
|Fan Wu|[fwu03](https://github.ubc.ca/MDS-2018-19/DSCI_522_proposal_fwu03)|
|Sreya Guha||

### Chicago Crimes Dataset
We will analyze the Chicago crimes dataset that reflects the crimes occurred in Chicago, USA from 2012-2017. The dataset includes following contents:

|Column Name|Description|
|--|--|
|||

We write a script to download the dataset as follow:
[need a screenshot here]

### Preductive Question

What are the strongest predictors of an arrest result for a crime in Chicago?  

### Data Analysis Plan

The goal of this analysis is to analyze the Chicago Crimes Dataset from 2012-2017, classify the features that determine the arrest result, and construct a prediction model to identify whether an arrest could happen for future crime. The detailed steps for this analysis are:

Step 1. Load data into Python

Step 2. Data wrangling:

- Checking missing values
- Dealing with null values
- Cleaning the description column with standard key words
- Putting the arrest and domestic columns into 1 or 0
- Separating the date and time.

Step 3. Visualiztions of the dataset:

- Which crime was maximum? 
- Location with highest crime rate
- Crimes trend among 2012-2017
- Summary of the arrest results

Step 4. Prediction Model: 

In this analysis, we will apply the linear regression model to find the strongest features that are able to predict the arrest result.

- Separate the dataset into training and testing dataset (7:3).
- Define the explanatory variable X to be a vector includes time of the crime, primary type, description, location, and domestic.
- Define the dependent variable Y to be the arrest result. 
- Use the linear regression to model the relationship between X and Y. 
- Once we get the equation, we can use it to get the predicted arrest results for the testing dataset, and compare them with the actual results to get the accurancy rate.


### Experimental Results

To present our result, we are going to use a table to show the coefficients for all variables and a graph to indicate the relationship between observations (points) and the regression model (a line). Besides, we will also examine the fitness of our model by calculating the R-squared value. 

