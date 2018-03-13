**Title** Logs analysis project, Udacity

**Description** 
This project is part of Udacity full stack nanodegree program wherein we answer 3 questions by querying the 'news' database which has a few prepopulated tables. We need to study the schema of respective tables, analyze the relationships between them and devise appropriate queries.
The questions are as follows:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

The main tool file is python program "news_db.py" which when executed (using python 3 interpretor) gives the answers to the questions using appropriate database queries.

Each of the database queries are implemented as separate functions. Each function creates a connection to the 'news' database and closes the connection at the end of the function.
The calls to the respective functions are in the bottom of the script. 
By default the script will run all 3 queries one after the other.
To run an individual query, uncomment the function call (for that particular query) and comment the other 2 function calls.

**Requirements / Dependencies**
You need to login to the Linux-based virtual machine (VM) provided by Udacity so that the python script can access the database server.

**Create views**
Currently no views are added to the database.

*TODO:* Update section with 'create view' commands when views are added to database as part of best practice. 

**How to execute**
There are 2 ways to execute the script.
1. (recommended) Execute on the terminal with python3: ** # python3 news_db.py **
2. Execute the script directly (ensure it has execute permissions set) ** # ./news_db.py **