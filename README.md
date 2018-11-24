# A Crime Data Analysis in Chicago

| **Team Members** |
| -- |
| Fan Wu |
| Sreya Guha |


### Chicago Crimes Dataset
We are going to analyze the Chicago crimes dataset that reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2016 to 2017. Data is extracted from the Chicago Police Department’s CLEAR (Citizen Law Enforcement Analysis and Reporting) system. In order to protect the privacy of crime victims, addresses are shown at the block level only and specific locations are not identified.
Essentially, this dataset contains the type of Crime, Location, Sub Category of the Crime, Type of Vicinity and Whether the arrest was possible or not.

The dataset includes the following contents:

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


We wrote a script to download the dataset as follows:

![image](https://github.com/UBC-MDS/DSCI522_sreya_fwu/blob/master/img/screenshot_data_load.png)


### Research Question

**What are the strongest predictors of an arrest result for a crime in Chicago?**

#### Type of question

This is a **predictive** question and we shall use a Decision Tree to answer the same.

### Dependencies
* R version 3.5.1
* R libraries:
    + tidyverse
    + ggplot2
    + dplyr
    + forcats
* Python version 3.6.5
* Python packages:
    + sys
    + pandas
    + matplotlib
    + numpy
    + pickle
    + graphviz
    + sklearn

### Project Objective
The goal of this analysis is to explore the Chicago Crimes Dataset from 2016-2017, classify the features that determine the arrest result, and construct a predictive model to identify whether an arrest could happen for a future crime.

### Data Analysis Plan
The detailed steps for this analysis are:

Step 1. Load data into Python

Step 2. Data wrangling:

- Checking null values and drop all of them
- Cleaning the description column with standard keywords
- Putting the arrest and domestic columns into 1 (True) or 0 (False)
- Separating the date and time into two columns.

Step 3. Visualizations of the dataset (EDA):

- The number of crimes type reported in the 2 years
- Location with the highest crimes
- Summary of the crime and arrest results

Step 4. Prediction Model: 

In this analysis, we will apply the decision tree method to find the strongest features that are able to predict the arrest result.

- Separate the dataset into training and testing datasets (7:3).
- Define the variable X to be a feature vector that includes the primary type (category of the crime), location.description, domestic, latitude, and longitude.
- Define the target variable Y to be the arrest result. 
- Use the decision tree package in Python (i.e. Scikit Learn) to model the relationship between X and Y. 
- Once we get the tree, we can use it to get the predicted arrest results for the testing dataset and compare them with the actual results to get the accuracy rate.
- Perform 10-fold cross validation and feature importance exam

### Experimental Results

The results of our analysis are summarized below:

- The decision tree has deepth of 5 and archives accuracy rate around 87%.
- The type of crime (i.e.Primary.Type), description of the location where the incident occurred (i.e.Location.Description) and whether the incident was domestic-related or not (Domestic) are the best indicators of an Arrest.

The detailed analysis is included in the [final report](https://github.com/UBC-MDS/DSCI522_sreya_fwu/blob/master/doc/report.md).

### Procedure
The project includes four major steps: data cleaning, data visualiztion, data analysis and data summarization. To generate the final report, the procedure is shown below:

![image](https://github.com/UBC-MDS/DSCI522_sreya_fwu/blob/master/img/project_flow_chart.png)

The purposes of the four scripts are:
- 01_data-clean.py: The script takes a raw crime dataset and generates a clean dataset through cleaning null values, updating data formats, and classifying data.
- 02_data-EDA.R: The script takes the clean crime dataset and generates data visualizations.
- 03_data-analysis.py: The script takes the clean crime dataset, select five specific columns as features, split the dataset as train and test sets (i.e. 7:3), and fit it into a decision tree model. The script also performs a 10-fold cross validation and features importance examine for the model and provides the corresponding scores.
- 04_data-summary.py: The script takes the model from 03_data-analysis.py and generates the corresponding decision tree.

### Usages
The usages of the scripts are:
```
# step 1. run 01_data-clean.py script: clean dataset
python src/01_data-clean.py data/crime_1617_raw_data.csv data/crime_1617_clean_data.csv

# step 2 . run 02_data-EDA.R script: perform EDA
Rscript src/02_data-EDA.R data/crime_1617_clean_data.csv img/

# step 3. run 03_data-analysis.py script: decision tree model
python src/03_data-analysis.py data/crime_1617_clean_data.csv results/

# step 4. run 04_data-summary.py script: modeling summary
python src/04_data-summary.py results/crime_1617_decisiontree_model.sav img/

# step 5. convert crime_tree.pdf to crime_tree.png
sips -s format png Crime_tree.pdf --out Crime_tree.png

# step 6. knit the final report.rmd
Rscript -e "rmarkdown::render('./doc/report.Rmd', 'github_document')"

```
Instead, you can also run the following code on command line to generate the final report under the root directory:

```
bash run_all.sh

```