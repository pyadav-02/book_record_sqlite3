from .sqlclass import Connection
BOOK_INFO = ('name', 'author', 'read')
DB = 'data.db'


def create_table():
    with Connection(DB) as connection:
        cursor = connection.cursor()
        cursor.execute("create table if not exists books(name text, author text, read text)")
    

def add_book(name, author):
    book_data = (name, author, "no")
    with Connection(DB) as connection:
        cursor = connection.cursor()
        cursor.execute("insert into books values(?, ?, ?)", book_data)


def list_book():
    book_data = None
    with Connection(DB) as connection:
        cursor = connection.cursor()
        cursor.execute("select * from books")
        book_data = cursor.fetchall()

    for row in book_data:
        print('-'*10)
        for key, value in zip(BOOK_INFO, row):
            print(f"{key}: {value}")
        
        

def delete_book(name, author):
    book_data = (name, author)
    with Connection(DB) as connection:
        cursor = connection.cursor()
        cursor.execute("delete from books where name = ? and author = ?", book_data)


def read_book(name, author):
    book_data = (name, author)
    with Connection(DB) as connection:
        cursor = connection.cursor()
        cursor.execute("update books set read = 'yes' where name = ? and author = ?", book_data)



