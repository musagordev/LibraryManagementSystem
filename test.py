class TestLibraryMethods(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    @patch('builtins.input', side_effect=["Book A", "Author A", "2020", "2"])
    def test_add_new_book(self, mock_input):
        # Test adding a new book
        self.library.add_book()
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Book A")
        self.assertEqual(self.library.books[0].author, "Author A")
        self.assertEqual(self.library.books[0].year, "2020")

    @patch('builtins.input', side_effect=["Book A", "Author A", "2020", "1", "Book B", "Author B", "2021", "2"])
    def test_add_multiple_books(self, mock_input):
        # Test adding multiple books
        self.library.add_book()
        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[0].title, "Book A")
        self.assertEqual(self.library.books[1].title, "Book B")

    @patch('builtins.input', side_effect=["Book A", "Author A", "2020", "3"])
    def test_invalid_choice_after_add(self, mock_input):
        # Test invalid choice handling
        self.library.add_book()
        self.assertEqual(len(self.library.books), 1)

    @patch('builtins.input', side_effect=['1', 'Y', '2'])
    def test_delete_existing_book(self, mock_input):
        # Create a library and add a book to it
        library = Library()
        library.books = [Book(1, "Test Book", "Test Author", 2024, "In Stock")]

        # Call delete_book to remove the book
        library.delete_book()

        # Verify that the library is now empty
        self.assertEqual(len(library.books), 0)

    @patch('builtins.input', side_effect=['2'])
    def test_delete_nonexistent_book(self, mock_input):
        # Create an empty library
        library = Library()

        # Try to delete a book that does not exist
        library.delete_book()

        # Verify that the library is still empty
        self.assertEqual(len(library.books), 0)

    @patch('builtins.input', side_effect=['1', 'N', '2'])
    def test_delete_book_canceled(self, mock_input):
        # Create a library and add a book to it
        library = Library()
        library.books = [Book(1, "Test Book", "Test Author", 2024, "In Stock")]

        # Call delete_book but cancel the deletion
        library.delete_book()

        # Verify that the book is still in the library
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0].title, "Test Book")
    
    @patch('builtins.input', side_effect=['1', '1', '2'])
    def test_search_by_id(self, mock_input):
        with patch('builtins.print') as mock_print:
            #Search ID 1 in library
            library = Library()
            library.books = [Book(1, "Test Book", "Test Author", 2024, "In Stock")]
            library.search_book()
            mock_print.assert_any_call('\n---Search Result of 1 in Id---')
    
    @patch('builtins.input', side_effect=['2', 'Test Book', '2'])
    def test_search_by__other_than_id(self, mock_input):
        with patch('builtins.print') as mock_print:
            #Search by title in library
            library = Library()
            library.books = [Book(1, "Test Book", "Test Author", 2024, "In Stock")]
            library.search_book()
            mock_print.assert_any_call('\n---Search Result of Test book in Title---')

    @patch('builtins.input', side_effect=['2', 'blabla', '2'])
    def test_search_book_not_found(self, mock_input):
        with patch('builtins.print') as mock_print:
            library = Library()
            library.books = [Book(1, "Test Book", "Test Author", 2024, "In Stock")]
            library.search_book()
            mock_print.assert_any_call('\nThere is no record found according to your search criteria!')
            
    @patch('builtins.input', side_effect=['1', '2', '2'])
    def test_change_status(self, mock_input):
        #Search status of book to issued
        library = Library()
        library.books = [Book(1, "Test Book", "Test Author", 2024, "In Stock")]
        library.change_status()
        self.assertEqual(library.books[0].status, "Issued")

            
if __name__ == '__main__':
    unittest.main()
