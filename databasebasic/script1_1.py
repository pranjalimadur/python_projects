import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS storage (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO storage VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

#insert("Coffee cup",15,6.99)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM storage")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(itm):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM storage WHERE item=?",(itm,))
    conn.commit()
    conn.close()

def update(quant,pr,itm):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE storage SET quantity=?, price=? WHERE item=?",(quant,pr,itm))
    conn.commit()
    conn.close()

update(7,8.99,"Coffee cup")
#delete("Wine Glass")
print(view())
