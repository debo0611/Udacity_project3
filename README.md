

The main tool file is python program "news_db.py" which needs to be executed using python 3 interpretor.

Execute on the terminal: python3 news_db.py 

Each of the database queries are implemented as separate functions. Each function creates a connection to the 'news' database and closes the connection at the end of the function.
The calls to the respective functions are in the bottom of the script. 
By default the script will run all 3 queries one after the other.
To run an individual query, uncomment the function call (for that particular query) and comment the other 2 function calls.