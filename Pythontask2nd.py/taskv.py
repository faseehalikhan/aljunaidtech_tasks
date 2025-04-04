def display_inventory(books):
    if not books:
        print("The inventory is empty.")
        return
    
    # Print table header
    print(f"{'ISBN':<20} {'Title':<30} {'Author':<20} {'Price':<10} {'Genres'}")
    print("=" * 90)  # Separator line

    # Loop through the dictionary and print details
    for isbn, details in books.items():
        title, author, price, genres = details  # Extract details
        genres_str = ", ".join(sorted(genres))  # Convert set to a sorted string
        
        # Print book details in formatted columns
        print(f"{isbn:<20} {title:<30} {author:<20} ${price:<10.2f} {genres_str}")

# Example dictionary of books
books = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 19.99, {"Fiction", "Adventure"}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 29.99, {"Education", "Technology"}),
    "978-0-12-345678-9": ("Mystery of the Night", "Emily Johnson", 15.50, {"Mystery", "Thriller"})
}

# Example usage
display_inventory(books)
