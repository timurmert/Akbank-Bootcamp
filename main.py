# ---------------------------------------------------------------------------------
# Library Management System
# Description: This Python script provides a simple library management system
#              which includes adding, listing, removing books, and counting 
#              the total number of books in the library. It uses a text file 
#              to store book data.
# Author: Timur Mert USTA, Sevde ŞEKEROĞLU 
# Group Name: HydRaboN
# Created on: 15.02.2024
# Last Modified: 16.02.2024
# Additions: Added a search_books method to search books by title or author.
# ---------------------------------------------------------------------------------

class Library:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if books:
            for book in books:
                name, author, year, pages = book.split(',')
                print(f"Name: {name}, Author: {author}, Year: {year}, Pages: {pages}")
        else:
            print("No books found.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter first release year: ")
        pages = input("Enter number of pages: ")
        self.file.write(f"{title},{author},{year},{pages}\n")
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter book title to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        books = [book for book in books if not book.split(',')[0] == title]
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines([book + "\n" for book in books])
        print("Book removed if it existed.")

    def search_books(self):
        query = input("Enter book title or author to search: ").lower()
        self.file.seek(0)
        found = False
        for book in self.file:
            if query in book.lower():
                print(book.strip())
                found = True
        if not found:
            print("No books found matching the query.")

def display_menu():
    print("*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Search Books\n")
    choice = input("Enter your choice: ")
    return choice

# Creating an instance
lib = Library('books.txt')

# Menu System
while True:
    choice = display_menu()

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        lib.search_books()
    else:
        print("Invalid choice.")
