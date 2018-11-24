# 02_data-EDA.R

# PURPOSE: The script takes the clean crime dataset and generates data visualizations
#
# ARGUMENTS:
#     ARG1 = input file path
#     ARG2 = output file path
#
# USAGE: "Rscript src/02_data-EDA.R data/crime_1617_clean_data.csv img/"

suppressPackageStartupMessages(library(tidyverse))
suppressPackageStartupMessages(library(ggplot2))
suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(forcats))

#get arguments
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]
output_file <- args[2]

# define the main function
main <- function(){
  #read clean data
  crime <- read.csv(input_file)
  
  # crime type analysis
  crime_type_count <- crime %>% 
    group_by(Primary.Type) %>% 
    summarise(counts=n()) %>%
    arrange(desc(counts)) 
  crime_type_count <- crime_type_count %>% 
    mutate(Primary.Type = fct_reorder(Primary.Type, counts))
  
  crime_type_plot <- generate_bar(crime_type_count, crime_type_count$Primary.Type, crime_type_count$counts, "Type of Crime", "Count", "Top crimes in 2016-2017")
  ggsave("crime_type_bar.png", plot = crime_type_plot, path = output_file,
         width = 6, height = 6)
  
  # crime location analysis
  crime_loc_count <- crime %>% 
    group_by(Location.Description) %>% 
    summarise(counts=n()) %>%
    arrange(desc(counts)) %>% 
    head(20)
  crime_loc_count <- crime_loc_count %>% 
    mutate(Location.Description = fct_reorder(Location.Description, counts))
  
  crime_loc_plot <- generate_bar(crime_loc_count, crime_loc_count$Location.Description, crime_loc_count$counts, "Location", "Count", "Location of crimes in 2016-2017")
  ggsave("crime_loc_bar.png", plot = crime_loc_plot, path = output_file,
         width = 6, height = 6)
  
  # crime per year
  crime_year <- crime %>% 
    group_by(Year, Primary.Type) %>%
    summarise(crime_count=n())
  # arrests per year
  arrest_year <- crime %>% 
    group_by(Year, Primary.Type) %>%
    filter(Arrest==1) %>%  
    summarise(arrest_count=n())
  # crime_arrests analysis
  crime_arrest_year <- left_join(crime_year,arrest_year)
  crime_arrest_year <- gather(crime_arrest_year, key = "crime_arrest", value = "value", arrest_count, crime_count)
  # plot
  crime_arrest_plot <- generate_bar_year(crime_arrest_year)
  ggsave("crime_arrest.png", plot = crime_arrest_plot, path = output_file,
         width = 6, height = 6)
}

generate_bar <- function(dataset, x, y, xlabel, ylabel, ttl){
  plot <- dataset %>% 
    ggplot(aes(x, y)) +
    geom_bar(stat="identity", fill="#800000") +
    theme_bw() +
    guides(fill=FALSE) +
    labs(title=ttl, x=xlabel, y=ylabel) +
    theme(axis.line = element_line(colour = "black"),
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.border = element_blank(),
          panel.background = element_blank()) +
    theme(axis.text.x=element_text(angle=90,hjust=1))
  return (plot)
}

generate_bar_year <- function(dataset){
  plot <- dataset %>% 
    top_n(35) %>% 
    ggplot(aes(x=Primary.Type, y=value, fill=crime_arrest)) +
    geom_bar(position = "dodge", stat="identity") +
    theme_bw() +
    theme(axis.line = element_line(colour = "black"),
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.border = element_blank(),
          panel.background = element_blank()) +
    scale_fill_manual(values=c("#0000A0","#800000")) +
    labs(title=paste("Number of arrests per crime"), x="Type of Crime", y="Number of arrests") +
    theme(axis.text.x=element_text(angle=90,hjust=1))
  return(plot)
}

# call main function
main()