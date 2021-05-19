from utils import database
import sys


User_Choice = """
Enter The Selection:
a. To add a new book
b. To list all books
c. To mark a book as read
d. To delete a book
q. To quit

Your Choice: """

def menu():
    user_input = ""
    user_input = input(User_Choice)
    if user_input == 'q':
        print("Terminating the program")
        sys.exit()
    while user_input != 'q':
        if user_input == 'a':
            adding_new_book_function()
        elif user_input == 'b':
            list_all_function()
        elif user_input == 'c':
            mark_as_read()
        elif user_input == 'd':
            delete_book()



def adding_new_book_function():
    book_name = input("Please enter the book title: ")
    author = input("Please enter the author name: ")
    database.adding_book(book_name, author)
    menu()

def list_all_function():
    books = database.list_book()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")
    menu()
def mark_as_read():
    user_input = input("Please enter book to mark as read: ")
    database.mark_read(user_input)
    print("Your request has been updated")
    menu()

def delete_book():
    user_input = input("What book would you like to delete from the list")
    database.delete_book_in_the_list(user_input)
    print(f"Deleting {user_input} in the database")
    menu()



menu()





























































































































































































































































































