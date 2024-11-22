import os
import json

class Book: #Create a Book class to keep information of book
    def __init__(self, id, title, author, year, status='In Stock'):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    
    def __str__(self):
        return (f'{self.id:<5} {self.title:<50} {self.author:<30} {self.year:<20} {self.status:<10}')

class Library: #Create a Library class for holding and managing information.
    #Books will be stored in List object
    def __init__(self):
        self.books = [] 
        self.logs = []
    
    #Loading library from json file.  
    def load_books(self, json_file):
        if not os.path.exists(json_file): #Checking if the file exist. If FileNotFound, the code will not raise an error, but it will ask user whether they want to create a new file.
            print(f'File not found! Do you like to create new library file as {json_file}?')
            print('1. Yes')
            print('2. No')
            choice = input('Your choice (1-2): ')
            if choice == '1':
                self.logs.append(f'# Creating a new file: {json_file} created successfully.')
                return []    #We will create empty list. This list will store json objects in library system.
        try: #We will use try-except block here to handle file not found error. If user didn't want to create new file we will print error message and return None.
            with open(json_file, 'r') as file:
                book_data = json.load(file)
                self.books = [Book(**book) for book in book_data] #Loading book datas from json_file and load to library
        except FileNotFoundError:
            print('File not found! Please check your file name and try again!')
            self.books = None
            return self.books
    
    #Update and save changes to the JSON file before exiting the program.
    def save_books(self, json_file):
        with open(json_file,'w') as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4) #Converting book objects to json file
            self.logs.append(f'Saving a file: # {json_file} saved successfully.')

    #Binary search for looking for ID. Our json file will store books according ids with ascending order. 
    #We will search our book_id with binary search to drop time complexity to O(logn). 
    def b_search(self, k):
        try: #User input must be book_id and all IDs are integer. Checking if input is numeric value.
            k = int(k)
        except ValueError:
            print('Error: ID must be a number!\n')
            return '-1'
        low = 0 #Inıtially we set low search parameter is 0 
        high = len(self.books)-1 #Inıtially we set high search parameter is highest index of json file
        mid = 0 #Initially we set our mid value 0 before computing
        while low <= high: #The binary search algorith continues until it finds position of book_id that we search. If low parameter will become higher than high parameter it will mean that book_id is not in library.
            mid = (low+high) // 2
            if int(self.books[mid].id) == k: #We are checking middle element of library's id is equal to id we are looking for.
                return self.books[mid]
            elif int(self.books[mid].id) < k: #If the id we are looking for is bigger than middle element of library's id, we will set low parameter one value higher than middle index. (Because we already checked middle element.)
                low = mid + 1
            elif int(self.books[mid].id) > k:#If the id we are looking for is lesser than middle element of library's id, we will set high parameter one value lower than middle index. (Because we already checked middle element.)
                high = mid - 1 
        return None 
    
    #Unique ID generator for library
    def generate_id(self):
        if not self.books:
            return 1
        new_id = max([int(book.id) for book in self.books])
        new_id += 1
        return new_id
        #Generate a unique ID for each book in the library without using external modules.
        #If library is empty, first book will have id=1, new books will have new id which will increment of max id
    
    #Adding a new book to Libray
    def add_book(self):
        print("\nPlease enter the information of the book which you would like to add to library\n")
        title = input("Title of the book: ").strip()
        author = input("Author of the book: ").strip()
        year = input("Publish year: ").strip()
        
        #If a book is already exist in the library, it will not be added it again. And provide feedback to users.
        for book in self.books:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower(): #Here we are checking if both title and author is same from input. Our reason is different authors may write book with same titles.
                print('\nThis book is already in library! Do you like to add another book?\n')
                print('1. Yes')
                print('2. No, return to Main Menu')
                after_choice = input('Your choice(1-2): ').strip()
                if after_choice == '1':
                    self.add_book()
                    return
                elif after_choice == '2':
                    print('You redirecting to Main Menu...\n')
                    return
                else:
                    print('Invalid choice! We are redirecting you to Main Menu...\n')
                    return
            
        book_id = self.generate_id()
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.logs.append(f'# Adding a new book: ID: {new_book.id}, Title: {new_book.title}, Author: {new_book.author} added to library successfully.')
        print(f"\n{title} added to library! ID: {book_id}\n")
        print('Do you like add another book?\n') #Asking user if he wants to add another book.
        print('1. Yes')
        print('2. No, return to Main Menu')
        after_choice = input('Your choice(1-2): ').strip()
        if after_choice == '1':
            self.add_book()
        elif after_choice == '2':
            print('You redirecting to Main Menu...\n')
            return
        else:
            print('Invalid choice! We are redirecting you to Main Menu...\n')
            return
    
    #Deleting a book from library
    def delete_book(self):
        if not self.books: #Check if there are any books in the library.
            print('\nThere is no book in library!\n')
            return
        book_id = input("\nPlease enter the id of the book you want to delete: ").strip()
        book = self.b_search(book_id) #Using b_search algorithm to find the book user want to delete
        if book is None: #Checking if book_id is not found.
            print('\nBook id is not found!\nPlease check book_id again!')
        elif book == '-1': #Checking if there is value error in the input.
            print('Please check book_id again!')
        else:  #If book is found, start the deletion process
            title = book.title
            final_choice = input(f"\nAre you sure that you want to delete {title}? Enter 'Y' or 'N':" ).strip() #Confirmation process before deleting book. We are asking Y or N here differently.
            if final_choice.capitalize() == 'Y':
                self.books.remove(book)
                self.logs.append(f'Deleting a book: # ID: {book.id}, Title: {book.title}, Author: {book.author} deleted from library successfully.')
                print(f'{title} deleted from library successfully')
            elif final_choice.capitalize() == 'N':
                print(f"{title} didn't deleted.")
            else:
                print('Invalid choice.')
        print('\nDo you want to delete another book?\n') #Asking user if he wants to delete another book.
        print('1. Yes')
        print('2. No, return to Main Menu')
        after_choice = input('Your choice(1-2): ').strip()
        if after_choice == '1': #Calling delete function again if user want to delete another book.
            self.delete_book()
        elif after_choice == '2': #If user doesn't want to delete another book, we are redirecting to main menu.
            print('You redirecting to Main Menu...\n')
            return
        else: #If user made invalid choice, we are giving feedback to user and redirecting main menu.
            print('Invalid choice! We are redirecting you to Main Menu...\n')
            return
    
    #Searching book in the library
    def search_book(self):
        if not self.books: #Check if there are any books in the library.
            print('\nThere is no book in library!\n')
            return
        print('\nPlease enter the number corresponding to category you would like to make a search from menu listed below between 1-5\n') #Asking user which category it would like to search in.
        print("1. Book ID")
        print("2. Title")
        print("3. Author")
        print("4. Publish Year")
        print("5. Status")
        
        choice=input("Category Choice: ").strip()
        
        category_map = { #We are creating category mapping to tell the program which choice user made.
            '1' : 'id',
            '2' : 'title',
            '3' : 'author',
            '4' : 'year',
            '5' : 'status'
        }

        if choice in category_map.keys(): #Checking if user made valid category choice.
            search_word = input(f'\nPlease enter the {category_map[choice]} you would like to search: ') #Receiving search parameter from user.
            category = category_map[choice]
        else:
            print('\nInvalid choice. Please choose a category between (1-5) corresponding to category name!')
            category, results = None, None

        #We are seperating book_id search from other categories with if-else block.
        if choice == '1': #If user would like to search with book_id, we are calling binary search algorithm.
            book = self.b_search(search_word)
            if book is None or book == '-1': #If book_id search is not found or there is an invalid input, we are returning empty result. Also invalid input returning error from b_search function.
                results= []
            else:  #If book found, we are returning book in the list.
                results = [book]        
        else: #For searches other than book_id we will check entire library to return matching books.
            if category is not None: #We are checking if user made the category search successfully. If it does we are searching matching books.
                results = [result for result in self.books if search_word.lower() in getattr(result,category).lower()]

        if results and results is not None: #Checking if any book found;
            print(f'\n---Search Result of {search_word.capitalize()} in {category.capitalize()}---')
            print(f"{'ID':<5} {'Title':<50} {'Author':<20} {'Publish Year':<20} {'Status':<10}") #Creating table headers with character limit for better interface for user.
            print("-" * 115)
            for book in results:
                print(book)
        elif results == []: #If no book found, results will return empty list.
            print('\nThere is no record found according to your search criteria!')
        
        print('\nDo you want to search another book?') #Asking user if user wants to search another book.
        print('1. Yes')
        print('2. No, return to Main Menu')
        after_choice = input('Your choice(1-2): ').strip()
        if after_choice == '1': #Calling search function again if user want to search another book.
            self.search_book()
        elif after_choice == '2': #If user doesn't want to search another book, we are redirecting to main menu.
            print('You redirecting to Main Menu...\n')
            return
        else: #If user made invalid choice, we are giving feedback to user and redirecting main menu.
            print('Invalid choice! We are redirecting you to Main Menu...\n')
            return    
    
    #Listing book in library
    def list_books(self):
        if not self.books: #Check if there are any books in the library.
            print('\nThere is no book in library!\n')
            return

        print(f"{'ID':<5} {'Title':<50} {'Author':<30} {'Publish Year':<20} {'Status':<10}") #Creating header before listing books
        print("-" * 115)
        for book in self.books: #Listing every book with character limit for better interface for user.
            print(book)
        leaving=input('\nPress Enter for returning to Main Menu: ')
    
    #Changing Status of Book
    def change_status(self):
        if not self.books: #Check if there are any books in the library.
            print('\nThere is no book in library!\n')
            return

        book_id = input("\nPlease enter the id of the book you want to change status: ").strip() #Ask the user which status they want to set for the book.
        book = self.b_search(book_id)
        if book is None: #Checking if book_id is not found.
            print('\nBook id is not found!\nPlease check book_id again!')
        elif book == '-1': #Checking if there is value error in the input.
            print('\nPlease check book_id again!')
        else: #If book found, process to change status will start.
            print(f"\n'Status of {book.title}': {book.status}") #Showing user current status of book.
            print(f'Please choose the status you want to set for the {book.title} from menu below and enter corresponding number') #Receiving choice from user which status user want to set for book.
            print('1. In Stock')
            print('2. Issued')
                
            choice = input('New status:' )
            if choice == '1':
                book.status = 'In Stock'
                print(f'\nStatus of {book.title} successfully updated as {book.status}!')
                self.logs.append(f'# Changing Status of book: {book.title} successfully updated as {book.status}!.')
            elif choice == '2':
                book.status = 'Issued'
                print(f'\nStatus of {book.title} successfully updated as {book.status}!')
                self.logs.append(f'# Changing Status of book: {book.title} successfully updated as {book.status}!.')
            else:
                'Invalid choice!'          
            
        print('\nDo you want to change status of another book?') #Asking user if user wants to change status of another book.
        print('1. Yes')
        print('2. No, return to Main Menu')
        after_choice = input('Your choice(1-2): ').strip()
        if after_choice == '1': #Calling changing status function again if user want to change status of another book.
            self.change_status()
        elif after_choice == '2': #If user doesn't want to change status of another book, we are redirecting to main menu.
            print('You redirecting to Main Menu...\n')
            return
        else: #If user made invalid choice, we are giving feedback to user and redirecting main menu.
            print('Invalid choice! We are redirecting you to Main Menu...\n')
            return 

    def list_logs(self):
        if not self.logs: #Check if there are any log in the library.
            print('\nThere is no book in library!\n')
            return

        for log in self.logs: #Listing every log with character limit for better interface for user.
            print(log)
        leaving=input('\nPress Enter for returning to Main Menu: ')

def main(data='data.json'):
    library = Library()
    data_file = data
    
    #Load datas from json file
    library.load_books(data_file)
        
    while True:
        if library.books is None:
            break
        print("\n---Library Management System---")
        print("\nWelcome to the Main Menu.\nPlease enter the number corresponding to the action you want to perform from below list. If you need any help please type 'help'\n")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. Search a Book")
        print("4. List all the Books")
        print("5. Change the Status of the Book")
        print('6. Show Logs')
        print("7. Exit")
        
        choice = input("Your choice (1-7): ")
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n---You are in the 'Add a Book' section.---")
            library.add_book()
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n---You are in the 'Delete a Book' section.---")
            library.delete_book()
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n---You are in the 'Search a Book' section.---")
            library.search_book()
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n---You are in the 'List a Book' section. Here is all the books in library---\n")
            library.list_books()
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n---You are in the 'Change the Status of the Book' section.---")
            library.change_status()
        elif choice == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n---You are in the 'Logs of the Library' section.---")
            library.list_logs()
        elif choice == '7':
            print("\nYou are leaving the library. Do you want to save your files?\n")
            print("1. Yes")
            print("2. No")
            choice = (input("Your choice (1-2): ")).strip()
            if choice == "1":
                print('Datas are saving...')
                library.save_books(data_file)
                break
            if choice == "2":
                print("Are you sure that you don't want to save your datas? The data will be lost and will not return back!")                
                final_choice = input("Type 'Y' for Yes, Type 'N' for No. Your choice(Y-N): ")
                if final_choice.capitalize() == 'Y':
                    break
                elif final_choice.capitalize() == 'N':
                    print("You are redirecting to Main Menu...")
                else:
                    print('Invalid choice. Please choose what you would like to do from Main Menu. You are redirecting to Main Menu...')
        elif choice == 'help':
            print("\nThis project is a Python-based Library Management System that allows users to manage books in a library.")
            print("In this program you can drive in the menu with typing corresponding numbers to your choice.")
            print("For example for adding a new book, you should type '1' which corresponding to adding a new book option in the main menu.")
            print("If you have more question. Please read README file on 'https://github.com/musagordev/LibraryManagementSystem/blob/main/README.md'")

            leaving=input('\nPress Enter for returning to Main Menu: ')
        else:
            print('Invalid choice. Please enter the number corresponding to the action you want to perform. ')

if __name__ == '__main__':
    main()
