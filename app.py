from database import add_book, get_all_books, delete_book, search_book, get_statistics

def main():
    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a Book")
        print("2. Display All Books")
        print("3. Remove a Book")
        print("4. Search a Book")
        print("5. Display Statistics")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == "1":
            book_name = input("Enter the name of the book: ")
            book_author = input("Enter the author of the book: ")
            published_year = input("Enter the published year: ")
            genre = input("Enter the genre of the book: ")
            read = input("Have you read it? (yes/no): ").strip().lower()
            
            book = {
                "title": book_name,
                "author": book_author,
                "published_year": published_year,
                "genre": genre,
                "status": "yes" if read == "yes" else "no"
            }
            add_book(book)
            print("✅ Book added successfully!")
        
        elif choice == "2":
            books = get_all_books()
            if not books:
                print("No books in the library.")
            else:
                for book in books:
                    print(f"\n**{book['title']}** by {book['author']}")
                    print(f"Published: {book['published_year']} | Genre: {book['genre']} | Read: {book['status']}")
        
        elif choice == "3":
            book_name = input("Enter the name of the book to remove: ")
            result = delete_book(book_name)
            if result.deleted_count > 0:
                print("✅ Book removed successfully!")
            else:
                print("⚠️ Book not found in the library.")
        
        elif choice == "4":
            book_name = input("Enter the name of the book to search: ")
            book = search_book(book_name)
            if book:
                print(f"\n✅ Found: {book['title']} by {book['author']}")
                print(f"Genre: {book['genre']} | Published: {book['published_year']} | Read: {book['status']}")
            else:
                print("⚠️ Book not found.")
        
        elif choice == "5":
            total_books, read_books, read_percentage = get_statistics()
            print(f"\n📊 Library Statistics")
            print(f"Total Books: {total_books}")
            print(f"Books Read: {read_books} ({read_percentage:.2f}%)")
        
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("⚠️ Invalid option, please try again!")

if __name__ == "__main__":
    main()
