from .database_connection import DatabaseConnection

book = []

def _create_table():
    with DatabaseConnection('book.db') as connection: #using class database connection to make it neat
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF  NOT EXISTS book (name text primary key, author text, read integer)')


def adding_book(name, author):
    with DatabaseConnection('book.db') as connection:
        cursor = connection.cursor()
        #cursor.execute(f'INSERT INTO book Values(?,?,0)', (name, author))
        cursor.execute('INSERT INTO book (name, author) VALUES (?, ?)', (name, author))
    print("Your book has been updated in the database")

def list_book():
    with DatabaseConnection('book.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM book')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    #books = cursor.fetchall()

    return books

def mark_read(name):
    with DatabaseConnection('book.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE book SET read = 1 WHERE name =?', (name,))


def delete_book_in_the_list(book_name):
    with DatabaseConnection('book.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM book WHERE name = ?', (book_name,))
