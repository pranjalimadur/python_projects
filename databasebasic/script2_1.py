import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS storage (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO storage VALUES(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()



def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM storage")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(itm):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM storage WHERE item=%s",(itm,))
    conn.commit()
    conn.close()

def update(quant,pr,itm):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE storage SET quantity=%s, price=%s WHERE item=%s",(quant,pr,itm))
    conn.commit()
    conn.close()

create_table()
#insert("Orange",10,15)
#insert("Apple",45,9)
#insert("Coffee bags",70,8)
#delete("Orange")
print(view())
update(20,7,"Apple")
#update(7,8.99,"Coffee cup")
#delete("Wine Glass")
#print(view())
#insert("Coffee cup",15,6.99)
