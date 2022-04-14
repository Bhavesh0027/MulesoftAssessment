import sqlite3
con= sqlite3.connect('MyMovie.db')
print(con) 

con.cursor()

#Insert values into table
con.execute("INSERT INTO MoviesINFO VALUES('Avengers','Tony stark','Scarlett','2020','Joe Russo')")
con.execute("INSERT INTO MoviesINFO VALUES('ABCD2','PrabhuDeva','Shraddha','2018','Remo Dsouza')")
con.execute("INSERT INTO MoviesINFO VALUES('RadheShyam','Prabhas','Pooja Hegde','2021','Radha Krishna Kumar')")
con.execute("INSERT INTO MoviesINFO VALUES('Bahubali','Prabhas','Anushka Shetty','2018','SS Rajamouli')")
print("Data added!")

#commit changes
con.commit()
con.close()