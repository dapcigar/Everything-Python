import pymysql as pydb

db = pydb.connect("localhost", "testuser","test123","testdb")
cusor = db.cursor()

cusor.execute("SELECT VERSION()")
