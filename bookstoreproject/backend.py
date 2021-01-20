import sqlite3

def connect():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("Dollar bahu","Sudha Murthy",2002,76236323732)
#insert("Wise and otherwise","Sudha Murthy",2006,28438534853)
#insert("When dimple met Rishi","Sandhya Menon",2005,26278484919)
#insert("White Tiger","Aravind Adiga",2008,38337385970)
#insert("2 states","Chtan bhagat",2006,19374859489)
#delete(5)
#update(2,"Wise and Otherwise","Sudha Murthy",2002,28485949288)
print(view())
#print(search(author="Sudha Murthy"))
