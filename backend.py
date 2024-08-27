import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS BOOK(ID INTEGER PRIMARY KEY, TITLE TEXT, AUTHOR TEXT, YEAR INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO BOOK VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM BOOK")
    rows=curr.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()

    # Add wildcards to allow for partial matches, and handle empty inputs.
    title = '%' + title.strip() + '%' if title else '%'
    author = '%' + author.strip() + '%' if author else '%'
    year = '%' + year.strip() + '%' if year else '%'
    isbn = '%' + isbn.strip() + '%' if isbn else '%'

    curr.execute("SELECT * FROM BOOK WHERE TITLE LIKE ? OR AUTHOR LIKE ? OR YEAR LIKE ? OR ISBN LIKE ?",
                 (title, author, year, isbn))

    res = curr.fetchall()
    conn.close()
    return res

def delete(id):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM BOOK WHERE ID=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("UPDATE BOOK SET title=?,author=?,year=?,isbn=? WHERE ID=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

# connect()

print(view())