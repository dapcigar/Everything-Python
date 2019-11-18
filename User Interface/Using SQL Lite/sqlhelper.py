import sqlite3


# Creating a Database in SQL lite using class
class SqliteHelper:
    def __init__(self, name=None):
        self.conn = None
        self.cusor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cusor = self.conn.cursor()
            # print(sqlite3.version)

        except sqlite3.Error as e:
            print(e)

    def create_table(self):
        c = self.cusor
        c.execute(""" CREATE TABLE users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        year INTEGER,
                        admin INTEGER)       
        
        """)

    def edit(self, query, updates): #Edit and insert
        c = self.cusor
        c.execute(query, updates)
        self.conn.commit()

    def delete(self, query): #Delete
        c = self.cusor
        c.execute(query)
        self.conn.commit()

    def insert(self, query, inserts):  #insert
        c = self.cusor
        c.execute(query,inserts)
        self.conn.commit()

    def select(self, query): #select
        c = self.cusor
        c.execute(query)
        return c.fetchall()




# instantiate the Class

# test = SqliteHelper("Test.db")

#Create Table in the DB using the Create Table Method
# test.create_table()

#Insert Into table using the Edit Method
# test.edit("INSERT INTO users (name, year, admin) VALUES('John', 1982, 0)")

#SELECT Value from  the Table
# res = test.select("SELECT * FROM users")
# print(res)

#EDIT data in the Table
# test.edit("UPDATE users SET name='Jack' WHERE name='John'")