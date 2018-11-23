
# coding: utf-8

# In[114]:


# 03_data-analysis.ipynb

# PURPOSE: The script takes the clean crime dataset and fit the dataset into decision tree model
#
# ARGUMENTS:
#     ARG1 = input file path
#     ARG2 = output file path
#
# USAGE: "python src/data_analysis.py data/crime_1617_clean_data.csv results/"


import pandas as pd
import numpy as np
import sys
import pickle

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import cross_val_score

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_analysis(input_file, output_file)
    

def mapping_ref(df, col):
    '''create reference mapping table'''
    temp_df = df[[col]]
    count_df = pd.DataFrame(temp_df.groupby(col).size().sort_values(ascending=False).rename('Count').reset_index())
    ref_df = count_df[col].values.tolist()
    return ref_df

def split_train_test(X,y,num):
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=num, random_state = 48)
    return Xtrain, Xtest, ytrain, ytest


def cross_validation(n, model, Xtest, ytest):
    cv_scores = cross_val_score(model, Xtest, ytest, cv=n)
    cv_score = np.mean(cv_scores)
    cv_df = pd.DataFrame({"index" : list(range(1,n+1)),
                          "cv_score": cv_scores})
    return cv_df


def decision_tree_model(df, feature_cols):
    #get X and y
    X = df.loc[:,feature_cols]
    y = df.Arrest
    Xtrain, Xtest, ytrain, ytest = split_train_test(X,y,0.3)
    
    #fit a decision tree model using sklearn
    model = tree.DecisionTreeClassifier(max_depth=5)
    model.fit(Xtrain,ytrain)
    predictions = model.predict(Xtest)
    
    #generate prediction summary
    pred_dict = Xtest.copy()
    pred_dict['Target'] = ytest
    pred_dict['Prediction'] = predictions
    
    #run 10-fold cross validation 
    cv_df = cross_validation(10, model, Xtest, ytest)
    
    return pred_dict, model, cv_df


def feat_importance(model, feature_cols):
    feat = model.tree_.compute_feature_importances(normalize=False)
    feat_df = pd.DataFrame([feat], columns = feature_cols)
    return feat_df

def export_csv(output_file, filename, df):
    df.to_csv(output_file + filename, index=False)
    
def data_analysis(input_file, output_file):
    #import clean data
    crime_df = pd.read_csv(input_file)
    
    # modify data types
    pt_ref = mapping_ref(crime_df, 'Primary.Type')
    loc_ref = mapping_ref(crime_df, 'Location.Description')
    crime_df['Primary.Type.Num'] = crime_df['Primary.Type'].apply(lambda x: pt_ref.index(x))
    crime_df['Location.Description.Num'] = crime_df['Location.Description'].apply(lambda x: loc_ref.index(x))
    
    #modeling by decision tree
    feature_cols = ['Primary.Type.Num','Location.Description.Num','Domestic','Latitude','Longitude']
    pred_dict, model, cv_df = decision_tree_model(crime_df, feature_cols)
    
    #for report purpose, we mapping the primary.type and location description back based on the reference tables
    pred_dict.insert(loc=0, column='Primary.Type', value=pred_dict['Primary.Type.Num'].apply(lambda x: pt_ref[x]))
    pred_dict.insert(loc=1, column='Location.Description', value=pred_dict['Location.Description.Num'].apply(lambda x: loc_ref[x]))
    pred_dict = pred_dict.drop(columns = ['Primary.Type.Num','Location.Description.Num'])
    
    #10-fold cross validation
    #cv_df = cross_validation(10, model, Xtest, ytest)
    
    #features importance
    feat_df = feat_importance(model, feature_cols)
    
    #save the model to disk
    model_file = output_file + "crime_1617_decisiontree_model.sav"
    pickle.dump(model, open(model_file, 'wb'))
    
    
    #export the results as csv file
    export_csv(output_file, "crime_1617_decisiontree_result.csv", pred_dict)
    export_csv(output_file, "crime_1617_decisiontree_cvscores.csv", cv_df)
    export_csv(output_file, "crime_1617_decisiontree_featuresimportance.csv", feat_df)
    
if __name__ == '__main__':
    main()  

