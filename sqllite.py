#import sqlite3 module
import sqlite3

#connect with database file
con= sqlite3.connect('MyMovie.db')
print(con)
print('Database opened!')
cur = con.cursor()

#create table name MoviesINFO
cur.execute('CREATE TABLE IF NOT EXISTS MoviesINFO(Movie VARCHAR,LeadActor TEXT,LeadActress TEXT,ReleaseYear INT,Director TEXT)')
print('Table created')

#commit changes
con.commit()
#close connection
con.close()
