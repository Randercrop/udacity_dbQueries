# udacity_dbQueries
Logs Analysis project for the Udacity Full Stack Web Development Nanodegree

This project runs database queries on a database provided by udacity.
The database can be downloaded [here] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


This project involves running three database queries on a set of data and printing out the result of the queries. The first query finds the top three most accessed articles in the database. The second query prints the list of authors in order of popularity, where popularity is determined by the cumulative number of hits each author receives. The last database query finds the dates where more than 1% of attempted "hits" failed with a 404 error. 


To run this project, 
  1. make sure the news_queries.py file is in the same directory as the newsdata.sql database.
  2. Initialize the database by running "psql -d news -f newsdata.sql"
  3. Run the python script with "python news_queries.py"
