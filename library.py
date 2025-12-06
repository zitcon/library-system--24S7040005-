library = []

def add_book():
    pass

def view_books():
    pass

def search_book():
    pass

def main():
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
def add_book():
    print("\n--- ADD NEW BOOK ---")
    title = input("Enter book title: ")
    author = input("Enter author: ")

    library.append({
        "title": title,
        "author": author,
        "is_available": True
    })

    print("Book added successfully.")

def view_books():
    print("\n--- BOOK LIST ---")
    if not library:
        print("Library is empty.")
        return
    for i, book in enumerate(library, start=1):
        status = "Available" if book['is_available'] else "Not available"
        print(f"{i}. {book['title']} | {book['author']} | {status}")
        
def search_book():
    query = input("Enter keyword: ").lower()
    found = False
    for book in library:
        if query in book["title"].lower():
            print(f"Found: {book['title']} by {book['author']}")
            found = True
    if not found:
        print("No matching books found.")
