def standardize_genres(books):
    # Iterate over every book in the dictionary
    for isbn, details in books.items():
        title, author, price, genres = details  # Extract book details

        # Standardize genres: lowercase and trim spaces
        standardized_genres = {genre.strip().lower() for genre in genres}

        # Update the dictionary with the new standardized genres
        books[isbn] = (title, author, price, standardized_genres)
    
    return "Genres standardized successfully."

# Example dictionary of books
books = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 19.99, {" Fiction ", "Adventure ", " ACTION"}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 29.99, {"Education", " Technology "}),
    "978-0-12-345678-9": ("Mystery of the Night", "Emily Johnson", 15.50, {"Mystery ", " thriller", "Crime "})
}

# Example usage
result = standardize_genres(books)

# Print the result and updated dictionary
print(result)
print(books)
