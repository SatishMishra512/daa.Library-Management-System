import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.books = []

        tk.Label(root, text="Title").grid(row=0, column=0)
        tk.Label(root, text="Author").grid(row=0, column=1)

        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=1, column=0)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)

        tk.Button(root, text="Add Book", command=self.add_book).grid(row=2, column=0)
        tk.Button(root, text="Show Books", command=self.show_books).grid(row=2, column=1)
        tk.Button(root, text="Remove Book", command=self.remove_book).grid(row=2, column=2)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.books.append(Book(title, author))
            messagebox.showinfo("Success", f"Book '{title}' by {author} added.")
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both title and author.")

    def show_books(self):
        if not self.books:
            messagebox.showinfo("Info", "No books in the library.")
            return
        books_list = "\n".join([f"Title: {book.title}, Author: {book.author}" for book in self.books])
        messagebox.showinfo("Books in Library", books_list)

    def remove_book(self):
        title = self.title_entry.get()
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                messagebox.showinfo("Success", f"Book '{title}' removed.")
                self.title_entry.delete(0, tk.END)
                self.author_entry.delete(0, tk.END)
                return
        messagebox.showerror("Error", "Book not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
