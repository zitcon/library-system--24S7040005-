# Global list to store data: each book is a dict {'title': '...', 'author': '...', 'is_available': True}
library = []

def add_book():
    # Tạm thời để trống, sẽ làm ở Feature 1
    pass

def view_books():
    # Sẽ làm ở Feature 2
    pass

def search_book():
    # Sẽ làm ở Feature 3
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
