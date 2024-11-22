# LibraryManagementSystem
This project is a Python-based Library Management System that allows users to manage books in a library. The system can store book details, search for books, update their status, and maintain all information in a JSON file. It provides a menu-driven interface for ease of use.
# Features
1. Add a Book: Add new books with details such as title, author, and publication year. The system generates a unique ID for each book.

2. Delete a Book: Remove books from the library using their unique ID.

3. Search for Books: Search for books by ID, title, author, publication year, or status.

4. List All Books: Display a list of all books in the library in a tabular format.

5. Change Book Status: Update the status of a book (e.g., "In Stock" or "Issued").

6. Data Persistence: Save and load book data in a JSON file for persistent storage

# Project Structure

 - **Book** Class: Represents individual books, with attributes for ID, title, author, publication year, and status.
 - **Library** Class: Handles the library's operations such as adding, deleting, searching, listing, and updating book information.
 - **main()** Function: Provides a menu-driven interface for interacting with the library.

# How to Run
1. Clone this repository or copy the code into a Python file, e.g., library_system.py.
   
`git clone musagordev/LibraryManagementSystem.git`

2. Make sure Python is installed on your machine.
  
3. Run the program using the command:

`python library_management.py`

4. Follow the on-screen instructions to interact with the library.

# Dependencies

- **Python 3.x**
- No other dependencies required

# Usage
**Adding a Book**
1. Choose the "Add a Book" option. (Option 1)
2. Provide details such as title, author, and publication year. 
3. The system will assign a unique ID to the book.

**Deleting a Book**
1. Choose the "Delete a Book" option. (Option 2)
2. Enter the book's unique ID.
3. Confirm the deletion.

**Searching for Books**
1. Choose the "Search a Book" option. (Option 3)
2. Select a search category (ID, title, author, year, or status).
3. Enter the search term to find matching books.

**Listing All Books**
1. Choose the "List All Books" option. (Option 4)
2. View all books in a tabular format.

**Changing Book Status**
1. Choose the "Change the Status of the Book" option. (Option 5)
2. Enter the book's unique ID.
3. Choose a new status ("In Stock" (1) or "Issued" (2).

**Exit the Library**
Choose the "Exit" option. (Option 6)

# File Storage
The program saves all book data to a JSON file (data.json) for persistence. If the file does not exist, the user will be prompted to create a new one.


