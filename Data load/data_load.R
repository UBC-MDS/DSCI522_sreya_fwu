data <- read.csv('../data/Chicago_Crimes_2012_to_2017.csv')

crime_16_17 <- data %>% 
  filter(Year>2015)

write.csv(crime_16_17, file = "crime_16_17.csv")
