def list_all_books(books):
    # Extract all book titles from the dictionary
    titles = [details[0] for details in books.values()]
    
    # Sort the titles alphabetically
    titles.sort()
    
    return titles

# Example dictionary of books
books = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 19.99, {"Fiction", "Adventure"}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 29.99, {"Education", "Technology"}),
    "978-0-12-345678-9": ("Mystery of the Night", "Emily Johnson", 15.50, {"Mystery", "Thriller"})
}

# Example usage
book_titles = list_all_books(books)

# Print the sorted list of book titles
print(book_titles)
