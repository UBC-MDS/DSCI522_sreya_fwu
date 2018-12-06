# run_all.sh

###################################################
## Date: November 23, 2018
## Author: Fan Wu
## Script purpose: This driver script completes the data analysis of the project.
##                 This script takes no arguments.
## Usage: bash run_all.sh
##################################################

# step 1. run 01_data-clean.py script: clean dataset
python src/01_data-clean.py data/crime_1617_raw_data.csv data/crime_1617_clean_data.csv

# step 2 . run 02_data-EDA.R script: perform EDA
Rscript src/02_data-EDA.R data/crime_1617_clean_data.csv img/

# step 3. run 03_data-analysis.py script: decision tree model
python src/03_data-analysis.py data/crime_1617_clean_data.csv results/

# step 4. run 04_data-summary.py script: modeling summary
python src/04_data-summary.py results/crime_1617_decisiontree_model.sav img/

# step 5. knit the final report.rmd
Rscript -e "rmarkdown::render('./doc/report.Rmd', 'github_document')"
