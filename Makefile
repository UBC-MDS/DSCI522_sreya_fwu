# Makefile
# author: Fan Wu & Sreya Guha
# Date: November 28, 2018
# Purpose: This script is use to automate our data analysis project pipline
# Useage:
# 		- make <specific script name>
#		- make all
#		- make clean

#####################################
# Run all scripts
#####################################

# run makefile using `Make` only, this command won't generate the dependency diagram
all_make: doc/report.md

# run makefile using `Docker`, this command will generate the dependency diagram
all: doc/report.md Makefile.png

#####################################
# Run Scripts
#####################################

DATASET = data/crime_1617_raw_data.csv
MODEL = results/crime_1617_decisiontree_model.sav results/crime_1617_decisiontree_cvscores.csv
PREDICTIONS = results/crime_1617_decisiontree_result.csv results/crime_1617_decisiontree_featuresimportance.csv
RESULT = img/crime_tree.png

# step 1. run 01_data-clean.py script: clean dataset
data/crime_1617_clean_data.csv : src/01_data-clean.py
		python src/01_data-clean.py $(DATASET) data/crime_1617_clean_data.csv

# step 2. run 02_data-EDA.R script: perform EDA
img/crime_arrest.png img/crime_loc_bar.png img/crime_month.png img/crime_type_bar.png : src/02_data-EDA.R data/crime_1617_clean_data.csv
		Rscript $^ img/

# step 3. run 03_data-analysis.py script: decision tree model
$(PREDICTIONS) $(MODEL): src/03_data-analysis.py data/crime_1617_clean_data.csv
		python $^ results/

# step 4. run 04_data-summary.py script: modeling summary
$(RESULT): src/04_data-summary.py $(MODEL)
		python src/04_data-summary.py results/crime_1617_decisiontree_model.sav img/

# step 5. knit the final report.rmd
doc/report.md: doc/report.rmd \
														img/crime_arrest.png \
														img/crime_loc_bar.png \
														img/crime_month.png \
														img/crime_type_bar.png \
														$(RESULT)
		Rscript -e "rmarkdown::render('./doc/report.Rmd')"

# step 6. Generate the dependency diagram (only for the Docker process)
Makefile.png: Makefile
	makefile2graph > Makefile.dot
	dot -Tpng Makefile.dot -o Makefile.png

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
		rm -f Makefile.png Makefile.dot
