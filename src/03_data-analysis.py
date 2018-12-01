
# coding: utf-8

# In[114]:


# 03_data-analysis.ipynb
# 
# TEAM: Fan Wu, Sreya Guha
# DATE: November 23, 2018
#
# PURPOSE: The script takes the clean crime dataset, select five specific columns as features, 
#          split the dataset as train and test sets (i.e. 7:3), and fit it into a decision tree model.
#          The script also performs a 10-fold cross validation and features importance examine for the 
#          model and provides the corresponding scores.
#
# INPUT:
#      - Clean Dataset: "data/crime_1617_clean_data.csv"
#
# OUTPUTS:
#      - Decision Tree Model: "results/crime_1617_decisiontree_model.sav"
#      - Prediction Results: "results/crime_1617_decisiontree_result.csv"
#      - Cross Validation Scores: "results/crime_1617_decisiontree_cvscores.csv"
#      - Features Importance: "results/crime_1617_decisiontree_featuresimportance.csv"
#
# ARGUMENTS:
#     ARG1 = input file path
#     ARG2 = output file path
#
# USAGE: "python src/03_data-analysis.py data/crime_1617_clean_data.csv results/"


import pandas as pd
import numpy as np
import sys
import pickle

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

def main():
    
    '''main function: grab the arg1 and arg2 as input file path and output file path '''
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_analysis(input_file, output_file)
    

def mapping_ref(df, col):
    
    '''create reference mapping table based on the provided dataframe'''
    
    temp_df = df[[col]]
    count_df = pd.DataFrame(temp_df.groupby(col).size().sort_values(ascending=False).rename('Count').reset_index())
    ref_df = count_df[col].values.tolist()
    return ref_df

def split_train_test(X,y,num):
    
    '''split the train and test datasets based on the test size provided (i.e. num)'''
    
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=num, random_state = 48)
    return Xtrain, Xtest, ytrain, ytest

def kfold_cv(Xtrain,ytrain):
    
    '''k-fold cross_validation function to find out the best depth for the tree'''
    
    accuracy = []
    depth = range(1, 20)
    for i in depth:
        model = tree.DecisionTreeClassifier(max_depth = i)
        model.fit(Xtrain, ytrain)
        accuracy.append(np.mean(cross_val_score(model, Xtrain, ytrain, cv = 5)))
    result_depth = depth[np.argmax(accuracy)]
    return result_depth

def kfold_plot(Xtrain,ytrain):
    
    '''function to plot k-fold cross_validation scores against the depth of the tree'''
    
    Accuracy = []
    Depth = range(1, 20)
    for i in Depth:
        model = tree.DecisionTreeClassifier(max_depth = i)
        model.fit(Xtrain, ytrain)
        Accuracy.append(np.mean(cross_val_score(model, Xtrain, ytrain, cv = 5)))
    k_fold_plot = plt.plot(Depth, Accuracy)
    plt.savefig("img/k_fold_plot.png")
    
def cross_validation(n, model, Xtest, ytest):
    
    '''cross_validation function is to exam the model accurcy based on the test set provided'''
    
    cv_scores = cross_val_score(model, Xtest, ytest, cv=n)
    cv_score = np.mean(cv_scores)
    cv_df = pd.DataFrame({"Index" : list(range(1,n+1)),
                          "Cross validation scores": cv_scores})
    return cv_df


def decision_tree_model(df, feature_cols):
    
    '''decision_tree_model function takes a dataframe and an array for features, fits a decision
       tree model with max_depth as 5, and provides prediction results for the test set'''
    
    #get X and y
    X = df.loc[:,feature_cols]
    y = df.Arrest
    Xtrain, Xtest, ytrain, ytest = split_train_test(X,y,0.3)
    
    #fit a decision tree model using sklearn
    #model = tree.DecisionTreeClassifier(max_depth=kfold_cv(Xtrain,ytrain))
    model = tree.DecisionTreeClassifier(max_depth=3)
    model.fit(Xtrain,ytrain)
    predictions = model.predict(Xtest)
    
    #generate prediction summary
    pred_dict = Xtest.copy()
    pred_dict['Target'] = ytest
    pred_dict['Prediction'] = predictions
    
    #run 10-fold cross validation 
    cv_df = cross_validation(10, model, Xtest, ytest)

    #plotting the depth of the tree vs. the cross validation accuracy
    kfold_plot(Xtrain,ytrain)
    
    return pred_dict, model, cv_df


def feat_importance(model, feature_cols):
    
    '''The feat_importance function takes a model and an array of features, and performs a 
       feature importance examine'''
    
    feat = model.tree_.compute_feature_importances(normalize=False)
    feat_df = pd.DataFrame([feat], columns = feature_cols)
    return feat_df

def export_csv(output_file, filename, df):
    
    '''export_csv function generate csv file at a specific output file path'''
    
    df.to_csv(output_file + filename, index=False)
    
def data_analysis(input_file, output_file):
    
    '''data_analysis function provides a general routine for a decision tree modeling'''
    
    #import clean dataset
    crime_df = pd.read_csv(input_file)
    
    # modify data types for `Primary.Type` and `Location.Description` to numerical values
    pt_ref = mapping_ref(crime_df, 'Primary.Type')
    loc_ref = mapping_ref(crime_df, 'Location.Description')
    crime_df['Primary.Type.Num'] = crime_df['Primary.Type'].apply(lambda x: pt_ref.index(x))
    crime_df['Location.Description.Num'] = crime_df['Location.Description'].apply(lambda x: loc_ref.index(x))
    
    #modeling by decision tree
    feature_cols = ['Primary.Type.Num','Location.Description.Num','Domestic','Latitude','Longitude']
    pred_dict, model, cv_df = decision_tree_model(crime_df, feature_cols)
    
    
    #for report purpose, we map the primary.type and location description back to categorical values based on the reference tables
    pred_dict.insert(loc=0, column='Primary.Type', value=pred_dict['Primary.Type.Num'].apply(lambda x: pt_ref[x]))
    pred_dict.insert(loc=1, column='Location.Description', value=pred_dict['Location.Description.Num'].apply(lambda x: loc_ref[x]))
    pred_dict = pred_dict.drop(columns = ['Primary.Type.Num','Location.Description.Num'])

    #cross validation scores
    cv_df = cv_df.round(2)

    #features importance examine
    feat_df = feat_importance(model, feature_cols).round(2)
    
    #save the model to disk
    model_file = output_file + "crime_1617_decisiontree_model.sav"
    pickle.dump(model, open(model_file, 'wb'))
    
    #export the results as csv files
    export_csv(output_file, "crime_1617_decisiontree_result.csv", pred_dict)
    export_csv(output_file, "crime_1617_decisiontree_cvscores.csv", cv_df)
    export_csv(output_file, "crime_1617_decisiontree_featuresimportance.csv", feat_df)

#call main function
if __name__ == '__main__':
    main()  

