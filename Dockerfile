# Docker file for A Crime Data Analysis in Chicago
# Authors: Fan Wu
# Time: December 6, 2018

# Description: This Makefile can be run to create our automatic data analysis pipeline

# Usage:
#   To build the docker image: docker build --tag dsci522_sreya_fwu:0.1 .
#   To create the report: docker run --rm -e PASSWORD=123456 -v `pwd`:/home/rstudio/dsci522_sreya_fwu:0.1 make -C '/home/rstudio/dsci522_sreya_fwu' all
#   To get a clean start: docker run --rm -e PASSWORD=123456 -v `pwd`:/home/rstudio/dsci522_sreya_fwu:0.1 make -C '/home/rstudio/dsci522_sreya_fwu' clean

# Use rocker/tidyverse as the base image
FROM rocker/tidyverse


# Install R packages
RUN Rscript -e "install.packages('tidyverse')"
RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('forcats')"
RUN Rscript -e "install.packages('lubridate')"

# Install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Get python package dependencies
RUN apt-get install -y python3-tk

# Install python packages
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install scikit-learn
#RUN pip3 install sys
#RUN pip3 install pickle
RUN apt-get install -y graphviz && pip install graphviz
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*
