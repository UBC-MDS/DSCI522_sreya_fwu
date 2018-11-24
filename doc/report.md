Crime analysis Report
================

Crime Analysis in Chicago
=========================

**Team:** Fan Wu & Sreya Guha

**Date:** November 23, 2018

Table of contents
-----------------

-   Introduction
-   Dataset
    -   Overview
    -   Data Wrangling
-   Exploratory Data Analysis
-   Prediction Model - Decision Tree
    -   Modeling
    -   Results
-   Limitations
-   References

Introduction
------------

The goal of the project is to analyze the Chicago crimes dataset and build a model that gives us the strongest predictors of an arrest result. Essentially, this dataset contains the type of Crime, Location, Sub Category of the Crime, Type of Vicinity and Whether the arrest was possible or not.

This project consists of two phases - Analyzing the dataset, Building a Decision Tree model.

Dataset
-------

### Overview

This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2016 to 2017. Data is extracted from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system. In order to protect the privacy of crime victims, addresses are shown at the block level only and specific locations are not identified. The data is in the following form:

*Table 1. Chicago Crime Raw Dataset*

|  X.1|     X|        ID| Case.Number | Date                   | Block                | IUCR | Primary.Type           | Description             | Location.Description | Arrest | Domestic |  Beat|  District|  Ward|  Community.Area| FBI.Code |  X.Coordinate|  Y.Coordinate|  Year| Updated.On             |  Latitude|  Longitude| Location                      |
|----:|-----:|---------:|:------------|:-----------------------|:---------------------|:-----|:-----------------------|:------------------------|:---------------------|:-------|:---------|-----:|---------:|-----:|---------------:|:---------|-------------:|-------------:|-----:|:-----------------------|---------:|----------:|:------------------------------|
|    1|     3|  10508693| HZ250496    | 05/03/2016 11:40:00 PM | 013XX S SAWYER AVE   | 0486 | BATTERY                | DOMESTIC BATTERY SIMPLE | APARTMENT            | True   | True     |  1022|        10|    24|              29| 08B      |       1154907|       1893681|  2016| 05/10/2016 03:56:50 PM |  41.86407|  -87.70682| (41.864073157, -87.706818608) |
|    2|    89|  10508695| HZ250409    | 05/03/2016 09:40:00 PM | 061XX S DREXEL AVE   | 0486 | BATTERY                | DOMESTIC BATTERY SIMPLE | RESIDENCE            | False  | True     |   313|         3|    20|              42| 08B      |       1183066|       1864330|  2016| 05/10/2016 03:56:50 PM |  41.78292|  -87.60436| (41.782921527, -87.60436317)  |
|    3|   197|  10508697| HZ250503    | 05/03/2016 11:31:00 PM | 053XX W CHICAGO AVE  | 0470 | PUBLIC PEACE VIOLATION | RECKLESS CONDUCT        | STREET               | False  | False    |  1524|        15|    37|              25| 24       |       1140789|       1904819|  2016| 05/10/2016 03:56:50 PM |  41.89491|  -87.75837| (41.894908283, -87.758371958) |
|    4|   673|  10508698| HZ250424    | 05/03/2016 10:10:00 PM | 049XX W FULTON ST    | 0460 | BATTERY                | SIMPLE                  | SIDEWALK             | False  | False    |  1532|        15|    28|              25| 08B      |       1143223|       1901475|  2016| 05/10/2016 03:56:50 PM |  41.88569|  -87.74952| (41.885686845, -87.749515983) |
|    5|   911|  10508699| HZ250455    | 05/03/2016 10:00:00 PM | 003XX N LOTUS AVE    | 0820 | THEFT                  | $500 AND UNDER          | RESIDENCE            | False  | True     |  1523|        15|    28|              25| 06       |       1139890|       1901675|  2016| 05/10/2016 03:56:50 PM |  41.88630|  -87.76175| (41.886297242, -87.761750709) |
|    6|  1108|  10508702| HZ250447    | 05/03/2016 10:35:00 PM | 082XX S MARYLAND AVE | 041A | BATTERY                | AGGRAVATED: HANDGUN     | STREET               | False  | False    |   631|         6|     8|              44| 04B      |       1183336|       1850642|  2016| 05/10/2016 03:56:50 PM |  41.74535|  -87.60380| (41.745354023, -87.603798903) |

This dataset has 276819 rows and 24 columns.

*Table 2. Chicago Crime Dataset Dictionary* ![image](../img/data_dict.png)

### Data Wrangling

The first step is to identify all null values in the dataset and remove all of them. The second step is to modify the datatypes for the below features since they have to be pre-processed in order to fit the model.

-   Primary.Type: mapping the categorical values to a numerical values
-   Location.Description: mapping the categorical values to a numerical values
-   Date: changing its datatype to Date
-   Domestic: changing the boolean values to 1/0
-   Arrest: changing the boolean values to 1/0

*Table 3. Chicago Crime Clean Dataset*

|  Unnamed..0|     X|        ID| Case.Number | Date                | Block                | IUCR | Primary.Type     | Description             | Location.Description |  Arrest|  Domestic|  Beat|  District|  Ward|  Community.Area| FBI.Code |  X.Coordinate|  Y.Coordinate|  Year| Updated.On             |  Latitude|  Longitude| Location                      | Crime\_Date | Crime\_Time |
|-----------:|-----:|---------:|:------------|:--------------------|:---------------------|:-----|:-----------------|:------------------------|:---------------------|-------:|---------:|-----:|---------:|-----:|---------------:|:---------|-------------:|-------------:|-----:|:-----------------------|---------:|----------:|:------------------------------|:------------|:------------|
|           1|     3|  10508693| HZ250496    | 2016-05-03 23:40:00 | 013XX S SAWYER AVE   | 0486 | SEXUAL ASSAULT   | DOMESTIC BATTERY SIMPLE | APARTMENT            |       1|         1|  1022|        10|    24|              29| 08B      |       1154907|       1893681|  2016| 05/10/2016 03:56:50 PM |  41.86407|  -87.70682| (41.864073157, -87.706818608) | 2016-05-03  | 23:40:00    |
|           2|    89|  10508695| HZ250409    | 2016-05-03 21:40:00 | 061XX S DREXEL AVE   | 0486 | SEXUAL ASSAULT   | DOMESTIC BATTERY SIMPLE | RESIDENCE            |       0|         1|   313|         3|    20|              42| 08B      |       1183066|       1864330|  2016| 05/10/2016 03:56:50 PM |  41.78292|  -87.60436| (41.782921527, -87.60436317)  | 2016-05-03  | 21:40:00    |
|           3|   197|  10508697| HZ250503    | 2016-05-03 23:31:00 | 053XX W CHICAGO AVE  | 0470 | PUBLIC INDECENCY | RECKLESS CONDUCT        | STREET               |       0|         0|  1524|        15|    37|              25| 24       |       1140789|       1904819|  2016| 05/10/2016 03:56:50 PM |  41.89491|  -87.75837| (41.894908283, -87.758371958) | 2016-05-03  | 23:31:00    |
|           4|   673|  10508698| HZ250424    | 2016-05-03 22:10:00 | 049XX W FULTON ST    | 0460 | SEXUAL ASSAULT   | SIMPLE                  | SIDEWALK             |       0|         0|  1532|        15|    28|              25| 08B      |       1143223|       1901475|  2016| 05/10/2016 03:56:50 PM |  41.88569|  -87.74952| (41.885686845, -87.749515983) | 2016-05-03  | 22:10:00    |
|           5|   911|  10508699| HZ250455    | 2016-05-03 22:00:00 | 003XX N LOTUS AVE    | 0820 | THEFT            | $500 AND UNDER          | RESIDENCE            |       0|         1|  1523|        15|    28|              25| 06       |       1139890|       1901675|  2016| 05/10/2016 03:56:50 PM |  41.88630|  -87.76175| (41.886297242, -87.761750709) | 2016-05-03  | 22:00:00    |
|           6|  1108|  10508702| HZ250447    | 2016-05-03 22:35:00 | 082XX S MARYLAND AVE | 041A | SEXUAL ASSAULT   | AGGRAVATED: HANDGUN     | STREET               |       0|         0|   631|         6|     8|              44| 04B      |       1183336|       1850642|  2016| 05/10/2016 03:56:50 PM |  41.74535|  -87.60380| (41.745354023, -87.603798903) | 2016-05-03  | 22:35:00    |

Exploratory Data Analysis
-------------------------

Before doing the modeling, we need some preliminary investigations of the dataset to identify its patterns.

First, we look at the top crime types in Chicago from 2016-2017.

*Figure 1. The Top Crime Types in Chicago* ![image](../img/crime_type_bar.png)

There were more Theft crime incidents (37.7%) compared to the rest of the offenses. Sexual assault cases came in at 20.2% followed by Arson (12.2%). We can also see drug cases at 4.2% followed by far by criminal trespass cases at 2.4%.

To continue, we want to know the hot locations were most crimes are reported.

*Figure 2. The Top Crime Locations in Chicago* ![image](../img/crime_loc_bar.png)

We can see that most crimes were committed on the streets (23.7% )followed by residences (16.2%) . And then both apartments (12.6%) and sidewals (8.9%). This figure shows that crime patterns were consistent over multiple regions.

Let's now compare the number of crimes with the number of arrests in 2016 and 2017.

*Figure 3. Compare Crime and Arrest* \#![image](../img/crime_arrest.png)

From the above plots we can see that the number of arrests recorded in each year is very less compared to the number of crimes. The instances of theft is 94556 whereas the number of arrests for theft is 8479. This means that only 8.9% of the accused actually were arrested. This is followed by cases for Sexual assault where only 20% of the criminals got arrested.

Prediction Model - Decision Tree
--------------------------------

### Modeling

The benefit of using Decision Tree models is that they are easily understood due to their graphical representation and the simple tests conducted at each node. The tree is built from a set of rules that partition the data by examining value frequency of attributes. At each node the attribute's value is evaluated and depending on the outcome it either takes a route to the next decision node or terminates in a leaf node. A leaf or terminal node indicates the examples of the predicted class.

This is suitable to our dataset which has features like Time, Location, Domestic crime which do not have a direct connection with one another. We thus conducted a Decision Tree analysis on the cleaned dataset for all types of crimes to see the best predictors for an arrest result in Chicago. The features we selected to are: Primary.Types, Location.Description, Domestic, Latitude, and Longitude.

Since two features above (i.e. Primary.Types, Location.Description) were categorical, we converted features into numerical values in the data wrangling section.

A decision tree can take many hyper-parameters. We performed our experiments with the parameters: \[max depth=5\] which gave us an accuracy around 87%, more details about this will be shown in the results section. At the end, more than 50 nodes were created, we can conclude that this tree can be used as a suitable predictor for arrest.

### Results

The final tree can be visualized below:

*Figure 4. Decision Tree* ![image](../img/Crime_tree.png)

We performed 10-fold cross validation to calculate the accuracy of our model. The table below shows the 10 cross validation scores:

*Table 4. Cross Validation Scores*

|     index|                              cv\_score|
|---------:|--------------------------------------:|
|         1|                              0.8736045|
|         2|                              0.8709463|
|         3|                              0.8712121|
|         4|                              0.8745181|
|         5|                              0.8702645|
|         6|                              0.8734547|
|         7|                              0.8745015|
|         8|                              0.8707790|
|         9|                              0.8711779|
|        10|                              0.8750332|
|  The aver|  age of above 10 scores is around 87%.|

To calculate the imprtant features we decided to use Scikit-learn's `feature_importances_`. This function computes the importance of a feature is computed as the (normalized) total reduction of the criterion brought by that feature. It is also known as the Gini importance.

*Table 5. Feature Importances*

|  Primary.Type.Num|  Location.Description.Num|   Domestic|  Latitude|  Longitude|
|-----------------:|-------------------------:|----------:|---------:|----------:|
|         0.0940989|                 0.0124246|  0.0022572|         0|          0|

Thus we conclude that the type of crime (i.e.Primary.Type), description of the location where the incident occurred (i.e.Location.Description) and whether the incident was domestic-related or not (Domestic) are the best indicators of an Arrest.

Limitations
-----------

First, due to the GitHub space constraint, we only used the dataset for 2016 and 2017. In fact, the entire dataset we downloaded from Kaggle is from 2012 to 2017. If we includes more years into our analysis, the results may change.

Additionally, due to the timing issue, we only performed a decision tree model and archieved a 87% accuracy rate. To implement it, we should perform more modelings such as linear regression model, logistic regression, and etc. Then, based on the assumptions of each model and its accuracy result, we can find the optimal model for this practice.

Lastly, in the decision tree model, we choose the maximum deepth to be 5 by considering the trade off between time complexity and accuracy rate. For future implementation, we can perform more analysis about this trade off and pick the optimal deepth level.

References
----------

1.  [Analysis and Prediction of Crimes in Chicago](https://github.com/cnreddy11/Analysis-and-Prediction-of-Crimes-in-Chicago/blob/master/Chicago%20Crimes%20Analysis.ipynb)
2.  [Crimes in Chicago - Kaggle](https://www.kaggle.com/currie32/crimes-in-chicago)
3.  [Predictive Analysis of Crimes in Chicago](http://sites.warnercnr.colostate.edu/cnreddy/predictive-analysis-crimes-chicago/)
4.  [Chicago Crime Mapping: Magic of Data Science and Python](https://hackernoon.com/chicago-crime-mapping-magic-of-data-science-and-python-f2ecad74a597)
