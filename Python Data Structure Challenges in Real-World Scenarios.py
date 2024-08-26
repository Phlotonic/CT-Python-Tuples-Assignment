# Task 1: Library System Enhancement

# Existing Library Data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, book):
    """
    Function to add a new book to the library.
    Ensures no duplicate books are added.
    
    Parameters:
    library (list): The list of books in the library.
    book (tuple): The book to be added, represented as a tuple (title, author).
    
    Returns:
    list: Updated library list.
    """
    # Check if the book already exists in the library
    if book in library:
        print(f"The book '{book[0]}' by {book[1]} is already in the library.")
    else:
        # Add the new book to the library
        library.append(book)
        print(f"The book '{book[0]}' by {book[1]} has been added to the library.")
    return library

def input_books(library):
    """
    Function to allow user to input new books into the library.
    
    Parameters:
    library (list): The list of books in the library.
    
    Returns:
    list: Updated library list.
    """
    while True:
        # Get user input for book title and author
        title = input("Enter the book title (or type 'exit' to stop): ")
        if title.lower() == 'exit':
            break
        author = input("Enter the book author: ")
        
        # Create a book tuple
        new_book = (title, author)
        
        # Add the book to the library
        library = add_book(library, new_book)
    
    return library

# Example usage
library = input_books(library)

# Print the updated library
print("Updated Library:", library)
