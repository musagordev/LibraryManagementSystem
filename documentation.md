---

# Documentation: Library Management System

## Overview

This project is a Python-based Library Management System that allows users to manage books in a library. The system can store book details, search for books, update their status, and maintain all information in a JSON file. It provides a menu-driven interface for ease of use.

---

## Table of Contents

1. [System Architecture](#system-architecture)  
2. [Classes and Methods](#classes-and-methods)  
3. [Usage Guide](#usage-guide)  
4. [Data Storage](#data-storage)  
5. [Error Handling](#error-handling)  
6. [Customization](#customization)  
7. [Future Improvements](#future-improvements)  

---

## System Architecture

The system follows a modular design with two main classes:  
1. **Book**: Represents an individual book in the library.  
2. **Library**: Handles operations related to book management.  

The `main()` function provides a menu-driven interface for user interaction.

### Workflow

1. The user interacts with the main menu.
2. Operations are routed through the `Library` class, which modifies the in-memory book list.
3. Data is saved to and loaded from a JSON file (`data.json`) for persistence. You can always use another json file for multiple libraries.

---

## Classes and Methods

### 1. **Book Class**
This class encapsulates the details of a book.

#### Attributes
- `id`: Unique identifier for the book (integer).
- `title`: Title of the book (string).
- `author`: Author of the book (string).
- `year`: Publication year (integer).
- `status`: Current status of the book (`"In Stock"` or `"Issued"`).

#### Methods
- `__init__(self, id, title, author, year, status)`: Initializes a new book instance.

---

### 2. **Library Class**
This class manages the collection of books and provides operations for book management.

#### Attributes
- `books`: List of `Book` objects
- `logs`: List of `Logs` 

#### Methods
- `add_book(self)`: Adds a new book to the library.
- `delete_book(self)`: Removes a book using its unique ID.
- `search_books(self)`: Searches for books by a specified field.
- `list_books(self)`: Returns a formatted list of all books.
- `change_status(self)`: Updates the status of a book.
- `list_logs(self)`: Returns a formatted list of all logs.
- `b_search(self,k)`: Binary search of id:'k' in all books.
- `save_to_file(self, file_name)`: Saves all book data to a JSON file.
- `load_from_file(self, file_name)`: Loads book data from a JSON file.

---

## Usage Guide

### Setup
1. Ensure Python 3.x is installed.
2. Clone this repository.
   
   ```bash
   git clone musagordev/LibraryManagementSystem.git
   ```
   
3. Save the code in a `.py` file (e.g., `library_management.py`).

### Running the Program
Execute the program with:
```bash
python library_management.py
```

### Menu Options
1. **Add a Book**: Input title, author, and publication year to add a book.
2. **Delete a Book**: Remove a book by entering its ID.
3. **Search a Book**: Search for books using attributes like ID, title, author, publish year and status.
4. **List All Books**: View all books in the library.
5. **Change Book Status**: Update a book's status to `"In Stock"` or `"Issued"`.
6. **List Logs**: Wiew all logs in the library
---

## Add a Book Function
1. Input title, author, and publication year to add a book respectively.
2. Program will check if this book is already added in library for preventing duplicates.
3. After add a book process done, program will ask if user would like to add a new book.
4. If user won't choose to add a new book, user will redirect to main menu

## Delete a Book Function
1. Input unique id of the book.
2. Program will search the book with binary search function and return the book or provide information to user if book is not found or there is an invalid input.
3. User must confirm if they wants to delete this book.
4. After delete a book process done, program will ask if user would like to delete another book.
5. If user won't choose to delete another book, user will redirect to main menu

## Search a Book
1. User must choose in which category they would like to search.
2. After choosing search category, user must input search word.
3. If category is id, program will use binary search function and return the book if it found, otherwise provide information to user if book is not found or there is an invalid input.
4. For other categories program will get the books corresponding to search word and category with simple for loop.
5. If there will be no book found provide information to user if book is not found or there is an invalid input.

## List All Books
1. User will view all books in a tabular format.

## Change Book Status
1. Input unique id of the book.
2. Program will search the book with binary search function and return the book or provide information to user if book is not found or there is an invalid input.
3. User must choose if book in stock or issued.
4. After change status of book process done, program will ask if user would like to change status of another book.
5. If user won't choose to change status of another book, user will redirect to main menu
   
## List Logs
User will view logs made in system.

## Exit
1. When user choose to exit, program will ask if user wants to save changes.
2. If user choose to exit without saving, program is printing a warning to user that all data will be lost and confirming user's decision.

## Data Storage

### JSON File Structure
The library data is stored in a JSON file (`data.json`). The structure is as follows:
```json
[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Author Name",
    "year": 2024,
    "status": "In Stock"
  }
]
```

#### File Operations
- The program reads from the JSON file at startup (if it exists).
- Changes made during execution are saved back to the file when exiting. User also has an option to exit without saving.

---

## Error Handling

- **Invalid Input**: The program validates user inputs for required formats (e.g., numeric fields).
- **File Not Found**: If the JSON file does not exist, the user is prompted to create a new one.
- **ID Errors**: Operations like delete or update validate the existence of a book with the given ID.

---
