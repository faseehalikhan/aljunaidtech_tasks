def search_by_author(author, books):
    # List to store matching books
    matching_books = []
    
    # Loop through the dictionary
    for isbn, details in books.items():
        if details[1] == author:  # Check if the author matches
            matching_books.append((isbn, details[0]))  # Add (ISBN, Title) to the list
    
    return matching_books  # Return the list of matching books

# Example dictionary of books
books = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 19.99, {"fiction", "adventure"}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 29.99, {"education", "technology"}),
    "978-0-12-345678-9": ("Mystery of the Night", "Emily Johnson", 15.50, {"mystery", "thriller"}),
    "978-3-16-148411-7": ("Another Adventure", "John Doe", 22.50, {"fiction", "action"})
}

# Example usage
author_name = "John Doe"
result = search_by_author(author_name, books)

# Print the results
print(result)  # Expected output: [("978-3-16-148410-0", "The Great Adventure"), ("978-3-16-148411-7", "Another Adventure")]
