def update_price(isbn, new_price, books):
    # Check if the ISBN exists in the dictionary
    if isbn in books:
        # Extract the existing book details
        title, author, _, genres = books[isbn]  # Extracting existing values except price
        
        # Create a new tuple with updated price
        books[isbn] = (title, author, new_price, genres)
        
        return f"Price updated successfully for ISBN {isbn}."
    else:
        return "ISBN not found in the inventory."

# Example dictionary of books
books = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 19.99, {"fiction", "adventure"}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 29.99, {"education", "technology"}),
    "978-0-12-345678-9": ("Mystery of the Night", "Emily Johnson", 15.50, {"mystery", "thriller"})
}

# Example usage
isbn_to_update = "978-3-16-148410-0"
new_price = 25.99

result = update_price(isbn_to_update, new_price, books)

# Print the result and updated dictionary
print(result)
print(books)
