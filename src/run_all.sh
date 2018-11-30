#! /usr/bin/env Rscript
# EDA.R
# Sreya Guha, Nov 2018

#some description

#example usage:
# bash run_all.sh

jupyter nbconvert --to script EDA1.ipynb
jupyter nbconvert --to script EDA2.ipynb
jupyter nbconvert --to script EDA3.ipynb
# create plots
Rscript src/EDA1.r data/crime_1617_clean_data.csv
Rscript src/EDA2.r data/crime_1617_clean_data.csv
Rscript src/EDA3.r data/crime_1617_clean_data.csv
python src/wordcount.py data/abyss.txt results/abyss.dat
python src/wordcount.py data/last.txt results/last.dat
python src/wordcount.py data/sierra.txt results/sierra.dat
python src/plotcount.py results/isles.dat results/figure/isles.png
python src/plotcount.py results/abyss.dat results/figure/abyss.png
python src/plotcount.py results/last.dat results/figure/last.png
python src/plotcount.py results/sierra.dat results/figure/sierra.png
Rscript -e "rmarkdown::render('doc/count_report.Rmd')"
