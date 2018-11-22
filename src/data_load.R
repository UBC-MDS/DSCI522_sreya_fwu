library(dplyr)

data <- read.csv('../data/crime_1617_raw_data.csv') 
# since this dataset is too large to load into Github, I have removed entries for 2012, 2013, 2014 and 2015 from the dataset.

# The code for removal of the afore mentioned years.
crime_16_17 <- data %>% 
  filter(Year>2015)

# I have now written this data into another dataset and this dataset has been uploaded to the repository.
write.csv(crime_16_17, file = "crime_16_17.csv")
