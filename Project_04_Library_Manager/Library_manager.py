import json
import os

data_file = "Library.txt"

def Load_Library():
    with open(data_file, "r") as file:
        return json.load(file)
    return []

def Save_Library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

def add_book(Library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read = input("Have you need the book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read" : read
    }

    Library.append(new_book)
    Save_Library(Library)
    print(f"Book {title} added succesfully.")

def remove_book(Library):
    title = input("Enter  the title of Book to remove from the Library")
    initial_lenght = len(Library)
    Library = [book for book in Library if book["title"].lower() != title]
    if len(Library) < initial_lenght:
        Save_Library(Library)
        print(f"Book {title} removed successfuly.")
    else:
        print(f"Book {title} not found in the Library")

def search_Library(Library):
    search_by = input("search by title or author").lower
    search_term = input(f"Enter the {search_by}").lower

    results = [Book for Book in Library if search_by in Book.values() and  search_term in Book[search_by].lower()]
    if results:
        for Book in results:
            status = "Read" if Book["read"] else "unread"
            print(f"{Book['title']} by {Book['author']} - {Book['year']} - {Book['genre']} - {status}")
    else:
        print(f"No Books found matching '{search_term}' in the {search_by} field.")

def list_books(Library):
    if Library:
        for book in Library:
            status = "Read" if book["read"] else "unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("No books in the library.")

def display_statistics(Library):
    total_books = len(Library)
    read_books = len([book for book in Library if book["read"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage of books read: {percentage_read:.2f}%")

def main():

    Library = Load_Library()

    while True:
        print("Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Library")
        print("4. List Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(Library)
        elif choice == "2":
            remove_book(Library)
        elif choice == "3":
            search_Library(Library)
        elif choice == "4":
            list_books(Library)
        elif choice == "5":
            display_statistics(Library)
        elif choice == "6":
            print("Goodbye!.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
