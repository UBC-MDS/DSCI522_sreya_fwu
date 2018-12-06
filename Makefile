# Makefile
# author: Fan Wu & Sreya Guha
# Date: November 28, 2018
# Purpose: This script is use to automate our data analysis project pipline
# Useage:
# 		- make <specific script name>
#		- make all
#		- make clean

#####################################
# Run Scripts
#####################################

# step 1. run 01_data-clean.py script: clean dataset
data/crime_1617_clean_data.csv : data/crime_1617_raw_data.csv src/01_data-clean.py
		python src/01_data-clean.py data/crime_1617_raw_data.csv data/crime_1617_clean_data.csv

# step 2. run 02_data-EDA.R script: perform EDA
img/crime_arrest.png img/crime_loc_bar.png img/crime_month.png img/crime_type_bar.png : data/crime_1617_clean_data.csv src/02_data-EDA.R
		Rscript src/02_data-EDA.R data/crime_1617_clean_data.csv img/

# step 3. run 03_data-analysis.py script: decision tree model
results/crime_1617_decisiontree_model.sav results/crime_1617_decisiontree_result.csv results/crime_1617_decisiontree_cvscores.csv results/crime_1617_decisiontree_featuresimportance.csv : data/crime_1617_clean_data.csv src/03_data-analysis.py
		python src/03_data-analysis.py "./data/crime_1617_clean_data.csv" "./results/"

# step 4. run 04_data-summary.py script: modeling summary
img/crime_tree.png : results/crime_1617_decisiontree_model.sav src/04_data-summary.py
		python src/04_data-summary.py results/crime_1617_decisiontree_model.sav img/

# step 5. knit the final report.rmd
doc/report.md doc/report.html : doc/report.rmd img/crime_arrest.png img/crime_loc_bar.png img/crime_month.png img/crime_type_bar.png img/crime_tree.png
		Rscript -e "rmarkdown::render('./doc/report.Rmd', 'github_document')"


#####################################
# Run all scripts
#####################################
all : doc/report.md

#####################################
# Remove all files
#####################################
clean:
		rm -f data/crime_1617_clean_data.csv
		rm -f img/crime_type_bar.png img/crime_loc_bar.png img/crime_arrest.png img/crime_month.png img/k_fold_plot.png
		rm -f results/crime_1617_decisiontree_model.sav results/crime_1617_decisiontree_result.csv results/crime_1617_decisiontree_cvscores.csv results/crime_1617_decisiontree_featuresimportance.csv
		rm -f img/crime_tree.png
		rm -f doc/report.md
		rm -f doc/report.html
