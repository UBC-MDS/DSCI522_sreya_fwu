
# coding: utf-8

# In[13]:


# 04_data-summary.ipynb
# 
# TEAM: Fan Wu
# DATE: November 23, 2018
#
# PURPOSE: The script takes the model from 03_data-analysis.py and generates the corresponding decision tree
#
# INPUT:
#    - Decision Tree Model: "results/crime_1617_decisiontree_model.sav"
#
# OUTPUT:
#    - Decision Tree Graph: "img/Crime_tree.pdf"
#
# ARGUMENTS:
#     ARG1 = input file path
#     ARG2 = output file path
#
# USAGE: "python src/04_data-summary.py results/crime_1617_decisiontree_model.sav img/"

import sys
import graphviz
import pickle

from sklearn.tree import export_graphviz
from sklearn import tree


def main():
    
    '''main function: grab the arg1 and arg2 as input file path and output file path '''
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_summary(input_file, output_file)

def save_and_show_decision_tree(model, feature_cols, class_names, save_file_prefix, **kwargs):
    
    '''Saves the decision tree model as a pdf '''

    dot_data = tree.export_graphviz(model, out_file=None, 
                             feature_names=feature_cols,  
                             class_names=class_names,  
                             filled=True, rounded=True,  
                             special_characters=True, **kwargs)  

    graph = graphviz.Source(dot_data, format = "png") 
    graph.render(save_file_prefix) 
    return graph

def data_summary(input_file, output_file):
    
    '''generates the decision tree model to a specific file path'''
    
    #load model
    model = pickle.load(open(input_file, 'rb'))
    feature_cols = ['Primary.Type.Num','Location.Description.Num','Domestic','Latitude','Longitude']
    
    #generate decision tree
    crime_tree = save_and_show_decision_tree(model,feature_cols, ['Target:1', 'Target:0'], output_file + 'crime_tree')

#call main function
if __name__ == '__main__':
    main() 

