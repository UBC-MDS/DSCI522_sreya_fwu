# Lab 1 - SQL basics

## Part 1 - Creating and modifying data (CREATE, INSERT,  DELETE, UPDATE, DROP)

Consider the following schemas:

* Movie(movideID: string, title: string, year: int, runningTime: int, genre: string, producer: string, principal: string) - Obs: `runningTime` should be in minutes and `principal` is the main actor/actress.
* People(personID: string, firstName: string, lastName: string, dateBirth: date, dateDeath: date)
* Producer(name: string, dateFounded: data, ceo: string)

### Exercise 1.1
rubric={reasoning:1}

From the fields in the schema above, what would you use as the primary key for each table? Why `Movie.title` wouldn't be a good primary key?

**Your answer**:

### Exercise 1.2 - Creating table
rubric={accuracy:1}

Fill in the code below to create the table `People` (don't forget to specify the primary key).

```sql
CREATE TABLE People(
    'personID' TEXT,
    'firstName' TEXT,
    'lastName' TEXT,
    'dateBirth' DATE,
    'dateDeath' DATE
);
```

### Exercise 1.3 - Creating table
rubric={accuracy:1}

Create the table `Producer` (don't forget to specify the primary key).

```sql
-- TODO: Replace this comment with your answer.
CREATE TABLE Producer('name' TEXT, 'dateFounded' TEXT, 'ceo' TEXT, PRIMARY KEY(name))
```

### Exercise 1.4 - Constraint and Referential Integrity 
rubric={accuracy:2}

Create the table `Movies`. Keep in mind the following points:

* Do not forget to specify the primary key;
* Specify the foreign keys for referential integrity using `CASCADE` option when deleting and updating;

```sql
-- TODO: Replace this comment with your answer.
CREATE TABLE Movies('movideID' TEXT, 'title' TEXT, 'year' INTEGER, 'runningTime' INTEGER, 'genre' TEXT, 'producer' TEXT, 'principal' TEXT, PRIMARY KEY())
```

### Exercise 1.5 - Inserting
rubric={accuracy:2}

Now, let's populate your tables. Insert at least four movies in the movie table. I will give you the first one as example. (Hint: SQLite has `foreign key` support disabled by default; to enforce the `foreign key` restriction, execute the code: `PRAGMA foreign_keys = ON;`)

* Insert into `Movies`: `("m01", "Joe Black", 1998, 178, "Drama", "Universal Studio", "p01");`
* Insert into `People`: `("p01", "Brad", "Pitt", "1963-12-18", NULL);`
* Insert into `Producer`: `("Universal Studio", "1912-04-30", "Ronald Meyer");`

Note that the order that you insert the rows matters due to the `foreign key` restrictions (try it!).

```sql
-- TODO: Replace this comment with your answer.
INSERT INTO Movies VALUES("m01", "Joe Black", 1998, 178, "Drama", "Universal Studio", "p01")
INSERT INTO Movies VALUES("m02", "Deadpool", 2016, 146, "Fantasy", "Marvel Entertainment", "p02")
INSERT INTO Movies VALUES("m03", "Ghost Rider", 2007, 114, "Fantasy", "Relativity Media", "p03")
INSERT INTO Movies VALUES("m04", "Hitch", 2005, 118, "Romance", "Overbrook Entertainment", "p04")
INSERT INTO Movies VALUES("m05", "Blended", 2014, 117, "Comedy", "Warner Bros", "p05")
```

### Exercise 1.6 - Updating
rubric={accuracy:1}

Oops, it seems that the example I gave you in the previous exercise was wrong. The name of the movie is "Meet Joe Black" and not "Joe Black". Update the value of the table accordingly. (Hint: Be careful to not change all the rows.)

```sql
-- TODO: Replace this comment with your answer.
UPDATE Movies 
SET title="Meet Joe Black"
WHERE movideID="m01" 
```

### Exercise 1.7 - (Optional) DBMS' Peculiarities 
rubric={reasoning:1,accuracy:1}

SQL is a language defined by International Organization for Standardization (ISO) and International Engineering Consortium (IEC). However, all the DBMS have proprietary features in addition to the SQL standard, and generally a DBMS does not fully comply with the SQL standard.

Let's check a peculiarity of SQLite in the following steps:
1. Create a table named `test` that has a column `firstName` with type `VARCHAR[5]`;
2. Insert a row using a string with length > 5;
3. Retrieve the row. What happened?
4. Delete the table;

Explain what happend and why. 

Your code:
```sql
-- TODO: Replace this comment with your answer.
```
Your reasoning:

## Part 2 - SELECT
The `SELECT` statement retrieves data from one or more tables. To practice some `SELECT` statements, use the database `cinema.db` in the file `cinema.7z` for this part.

### Exercise 2.1  - selecting sigle column
rubric={accuracy:1}

Fill in the code below to retrieve the primary title of 30 movies from the table `titles`.

```sql
SELECT primaryTitle
    FROM titles
    LIMIT 30;
```

(Note: The `LIMIT` clause just limits the number of rows retrieved and it was added to not inundate your screen).

### Exercise 2.2  - selecting multiple columns
rubric={accuracy:1}

Fill in the code below to retrieve the primary title, the year of release, and the run time of 30 movies from the table `titles`.

```sql
SELECT primaryTitle, startYear, runTimeMinutes
    FROM titles
    LIMIT 30;
```

### Exercise 2.3 - selecting all columns
rubric={accuracy:1}

Use the `*` placeholder to retrieve all columns from the table `people`.

```sql
-- TODO: Replace this comment with your answer.
SELECT *
FROM people;
```

(PS: Use `*` with care. It will probably retrieve unnecessary data, and also it makes your code hard to read if one is not familiarized with the tables.)

### Exercise 2.4 - using aliases
rubric={accuracy:1}

You can use `AS` to create alias for the columns in the output of your query (this does not permanently rename the columns in the table). Use `SELECT` query to retrieve `tconst`, `primaryTitle` and `startYear` from the table `titles`. Use the following alias `tconst` -> `titleID`, `primaryTitle` -> `Title`, and `startYear` -> `Year`. 

```sql
-- TODO: Replace this comment with your answer.
SELECT tconst AS titleID, primaryTitle AS Title, startYear AS Year
FROM titles;
```

### Exercise 2.5 - filtering
rubric={accuracy:1}

The `SELECT` statement will return all the rows unless otherwise specified. Use the `WHERE` clause to retrieve from the table `ratings`, the columns `tconst`, `averageRating`, and `numVotes`, of all movies with `averageRating` higher than 9.3.

```sql
-- TODO: Replace this comment with your answer.
SELECT tconst, averageRating, numVotes
FROM ratings
WHERE averageRating>9.3;
```

### Exercise 2.6 - filtering
rubric={accuracy:1}

Retrieve from the table `people` all the info (`*`) of those who were born after 1985 and have died (you can assume that a person has died only if the `deathYear` isn't `NULL`).

```sql
-- TODO: Replace this comment with your answer.
SELECT *
FROM people
WHERE (birthYear>1985) AND
      (deathYear IS NOT NULL);
```

### Exercise 2.7 - new (derived) columns
rubric={accuracy:1}

Use the `birthYear` and `deathYear` to calculate the approximate age at death for each person in table `people`. Use alias (see `AS`) to name this column `death_age`. Also, remove all entries with `NULL` `death_age`.

```sql
SELECT *, (deathYear-birthYear) AS death_age
FROM people
WHERE death_age IS NOT NULL;
```

## Part 3 - Joins

### Exercise 3.1 - using where for joins
rubric={accuracy:4}

Use `WHERE` clause to retrieve the columns `tconst`, `titleType`, `primaryTitle`, `startYear` from `titles` and  `averageRating` from `ratings` for all the movies in `titles` that have an `averageRating` higher than 9.

```sql
-- TODO: Replace this comment with your answer.
SELECT t.tconst, t.titleType, t.primaryTitle, t.startYear, r.averageRating
FROM titles t
LEFT JOIN ratings r
ON t.tconst=r.tconst
WHERE r.averageRating>9;
```

### Exercise 3.2 - using the `LEFT JOIN` clause
rubric={accuracy:4}

In the `cinema.db` database, there are only movies released after 1980. However, there are people that died before 1980 that were "involved" in the movies. How can that be? Use the `LEFT JOIN` clause to retrieve the columns `nconst` and `category` from the `principals` table, and `primaryName` and `deathYear` from `people` table, of all those people that died before 1980. Take a look at the role in the `category` column to understand why. (Hint: you might want to use `DISTINCT`).

```sql
-- TODO: Replace this comment with your answer.
SELECT DISTINCT pr.nconst, pr.category, p.primaryName, p.deathYear
FROM principals pr
LEFT JOIN people p
ON pr.nconst=p.nconst
WHERE p.deathYear<1980;
```

## Part 4 - Embedding SQL in R

[This resource](https://db.rstudio.com/databases/sqlite/) will be helpful to help you go throught this part.

### Exercise 4.1 - warm up
rubric={accuracy:2}

The first step is to create a connection using `RSQlite` package. To start create a connection with a new database named `flights.db` database. Then, save the tibbles `airports`, `planes` and `flights` of `nycflights13` package. (Hint: See `dbWriteTable()` and remember to call `dbDisconnect()`)

```R
library(DBI)
library(RSQLite)
library(nycflights13)
connection <- dbConnect(SQLite(), "flights.db")
dbListTables(connection)
dbWriteTable(connection, "airports", airports)
dbWriteTable(connection, "planes", planes)
dbWriteTable(connection, "flights", flights)
dbListTables(connection)
dbDisconnect(connection)
```

### Exercise 4.2 - the real thing!

Download the [full airline data from 2008](http://stat-computing.org/dataexpo/2009/2008.csv.bz2). You can do this the normal way through your browser. Or, if you want, you can also use a command line tool such as `wget`. For example, `wget http://stat-computing.org/dataexpo/2009/2008.csv.bz2` will download the 2008 data (2008 data is about 657MB). You will have to decompress the file using a tool such as `bunzip2` (the 7zip should be able to do it as well). There are 7,009,728 rows in 2008 data. Info about the columns can be found [here](http://stat-computing.org/dataexpo/2009/the-data.html).

Now, try loading the data into R using the base `read.csv`. What happened?
For some of you, the data might not even fit into memory. For others, it will be painfully slow.
Therefore, we will work with it in an SQL database using the RSQLite package. To help you set up the database, execute the following code in your SQLite (where `2008.csv` is the name of the file):

```sql

CREATE TABLE `flights` (
  `Year` INTEGER,
  `Month` INTEGER,
  `DayofMonth` INTEGER,
  `DayOfWeek` INTEGER,
  `DepTime` INTEGER,
  `CRSDepTime` INTEGER,
  `ArrTime` INTEGER,
  `CRSArrTime` INTEGER,
  `UniqueCarrier` TEXT,
  `FlightNum` INTEGER,
  `TailNum` TEXT,
  `ActualElapsedTime` INTEGER,
  `CRSElapsedTime` INTEGER,
  `AirTime` INTEGER,
  `ArrDelay` INTEGER,
  `DepDelay` INTEGER,
  `Origin` TEXT,
  `Dest` TEXT,
  `Distance` INTEGER,
  `TaxiIn` INTEGER,
  `TaxiOut` INTEGER,
  `Cancelled` INTEGER,
  `CancellationCode` TEXT,
  `Diverted` INTEGER,
  `CarrierDelay` INTEGER,
  `WeatherDelay` INTEGER,
  `NASDelay` INTEGER,
  `SecurityDelay` INTEGER,
  `LateAircraftDelay` INTEGER
);

.mode csv
.import 2008.csv flights
DELETE FROM flights 
    WHERE typeof(year) = "text";

UPDATE flights SET depTime = NULL WHERE (typeof(depTime) = 'text');
UPDATE flights SET ArrTime = NULL WHERE (typeof(Arrtime) = 'text');
UPDATE flights SET TailNum = NULL WHERE (Tailnum = '');
UPDATE flights SET ActualElapsedTime = NULL WHERE (typeof(ActualElapsedTime) = 'text');
UPDATE flights SET CRSElapsedTime = NULL WHERE (typeof(CRSElapsedTime) = 'text');
UPDATE flights SET AirTime = NULL WHERE (typeof(AirTime) = 'text');
UPDATE flights SET ArrDelay = NULL WHERE (typeof(ArrDelay) = 'text');
UPDATE flights SET DepDelay = NULL WHERE (typeof(DepDelay) = 'text');
UPDATE flights SET TaxiIn = NULL WHERE (typeof(TaxiIn) = 'text');
UPDATE flights SET TaxiOut = NULL WHERE (typeof(TaxiOut) = 'text');
UPDATE flights SET CancellationCode = NULL WHERE (CancellationCode = '');
UPDATE flights SET CarrierDelay = NULL WHERE (typeof(CarrierDelay) = 'text');
UPDATE flights SET WeatherDelay = NULL WHERE (typeof(WeatherDelay) = 'text');
UPDATE flights SET NASDelay = NULL WHERE (typeof(NASDelay) = 'text');
UPDATE flights SET SecurityDelay = NULL WHERE (typeof(SecurityDelay) = 'text');
UPDATE flights SET LateAircraftDelay = NULL WHERE (typeof(LateAircraftDelay) = 'text');
```

Now, using R, perform the following tasks (note that you can use the `dplyr` verbs you learned in DSCI 523 - Data Wrangling):

library(DBI)
library(RSQLite)
library(tidyverse)
connection <- dbConnect(SQLite(), "new_flights.db")
dbListTables(connection)
flight_4.2<-tbl(connection,"flights")

#### Exercise 4.2.1
rubric={accuracy:4}

Report the 10 busiest airports in terms of the number of departure flights. (If you want, you can compare your results to the [Wikipedia](https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States). You can find the airport code [here](http://stat-computing.org/dataexpo/2009/supplemental-data.html) ).

```R
#TODO
query <- flight_4.2 %>% 
  group_by(Origin) %>% 
  summarize(tot_flight=n()) %>% 
  arrange(desc(tot_flight))
airport_busy <- collect(query)
airport_busy %>% 
  top_n(10,tot_flight)
```

#### Exercise 4.2.2  
rubric={accuracy:4}

Retrieve all flights where the arrival time was delayed by more than 30 minutes. Summarize the delays by producing an appropriate figure, in a way that highlights the differences between airports (consider only airports that had more than 2500 flights delayed more than 30 min).

```R
#TODO
query1 <- flight_4.2 %>% 
  group_by(Dest) %>% 
  filter(ArrDelay>30) %>% 
  summarize(tot_flights=n()) %>%
  filter(tot_flights>2500) %>% 
  arrange(desc(tot_flights))
flight_delay <- collect(query1)
flight_delay
```

