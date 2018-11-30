
library(dplyr)
#install.packages("ggplot2")
library(ggplot2)
library(tidyr)
library(forcats)

args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]

# reading the data from "../data/crime_1617_clean_data.csv"
crime <- read.csv(input_file)
crime %>%
  head(15)

(crime_count <- crime %>%
  group_by(Primary.Type) %>%
  summarise(counts=n()) %>%
  arrange(desc(counts)) )

#(crime_co_plot <- crime_count %>%
#  head(10))

options(repr.plot.width = 7, repr.plot.height = 6)

crime_count %>%
  mutate(Primary.Type = fct_reorder(Primary.Type, counts)) %>%
  ggplot(aes(x=Primary.Type, y=counts)) +
  geom_bar(stat="identity", fill="#800000") +
  theme_bw() +
  guides(fill=FALSE) +
  labs(title="Top crimes in 2016-2017", x="Type of Crime", y="Count") +
  theme(axis.line = element_line(colour = "black"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.border = element_blank(),
    panel.background = element_blank()) +
  theme(axis.text.x=element_text(angle=90,hjust=1))

(crime_location <- crime %>%
  group_by(Location.Description) %>%
  summarise(counts=n()) %>%
  arrange(desc(counts)) %>%
  head(20))

crime_loc_plot <- crime_location %>%
  head(20)

options(repr.plot.width = 7, repr.plot.height = 6)

crime_loc_plot %>%
  mutate(Location.Description = fct_reorder(Location.Description, counts)) %>%
  ggplot(aes(x=Location.Description, y=counts)) +
  geom_bar(stat="identity", fill="#800000") +
  theme_bw() +
  guides(fill=FALSE) +
  theme(axis.line = element_line(colour = "black"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.border = element_blank(),
    panel.background = element_blank()) +
  labs(title="Location of crimes in 2016-2017", x="Location", y="Count") +
  theme(axis.text.x=element_text(angle=90,hjust=1))


# Counting the number of crimes per year
(crime_year <- crime %>%
  group_by(Year, Primary.Type) %>%
  summarise(crime_count=n()))

# Counting the number of arrests per year
(arrest_year <- crime %>%
  group_by(Year, Primary.Type) %>%
  filter(Arrest==1) %>%
  summarise(arrest_count=n()))

# Obtaining the crime count and arrest count for each type of crime per year
crime_arrest_year <- left_join(crime_year,arrest_year)
crime_arrest_year <- gather(crime_arrest_year, key = "crime_arrest", value = "value", arrest_count, crime_count)
crime_arrest_year %>% head(10)

options(repr.plot.width = 7, repr.plot.height = 6)

crime_arrest_year %>%
  top_n(35) %>%
  filter(Year==2016) %>%
  ggplot(aes(x=Primary.Type, y=value, fill=crime_arrest)) +
  geom_bar(position = "dodge", stat="identity") +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.border = element_blank(),
    panel.background = element_blank()) +
  scale_fill_manual(values=c("#0000A0","#800000")) +
  labs(title="Number of arrests per crime in 2016", x="Type of Crime", y="Number of arrests") +
  theme(axis.text.x=element_text(angle=90,hjust=1))

crime_arrest_year %>%
  filter(Year==2017) %>%
  ggplot(aes(x=Primary.Type, y=value, fill=crime_arrest)) +
  geom_bar(position = "dodge", stat="identity") +
  theme_bw() +
  theme(axis.line = element_line(colour = "black"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.border = element_blank(),
    panel.background = element_blank()) +
  scale_fill_manual(values=c("#0000A0","#800000")) +
  labs(title="Number of arrests per crime in 2017", x="Type of Crime", y="Number of arrests") +
  theme(axis.text.x=element_text(angle=90,hjust=1))

(crime %>%
  #top_n(35) %>%
  filter(Year==2017))
