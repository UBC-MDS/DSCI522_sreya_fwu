
# coding: utf-8

# In[13]:


# 04_data-summary.ipynb

# PURPOSE: The script takes the model from 03_data-analysis.py and then generates the physical decision tree
#
# ARGUMENTS:
#     ARG1 = input file path
#     ARG2 = output file path
#
# USAGE: "python src/data_summary.py results/crime_1617_decisiontree_model.sav img/"

import sys
import graphviz
import pickle

from sklearn.tree import export_graphviz
from sklearn import tree


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_summary(input_file, output_file)

def save_and_show_decision_tree(model, feature_cols, class_names, save_file_prefix, **kwargs):
    """
    Saves the decision tree model as a pdf and a 
    """
    dot_data = tree.export_graphviz(model, out_file=None, 
                             feature_names=feature_cols,  
                             class_names=class_names,  
                             filled=True, rounded=True,  
                             special_characters=True, **kwargs)  

    graph = graphviz.Source(dot_data) 
    graph.render(save_file_prefix) 
    return graph

def data_summary(input_file, output_file):
    #load model
    model = pickle.load(open(input_file, 'rb'))
    feature_cols = ['Primary.Type.Num','Location.Description.Num','Domestic','Latitude','Longitude']
    
    crime_tree = save_and_show_decision_tree(model,feature_cols, ['Target:1', 'Target:0'], output_file + 'Crime_tree')
    
if __name__ == '__main__':
    main() 

