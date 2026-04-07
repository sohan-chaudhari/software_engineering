class library:
    def issue_book(self,book_name,is_available):
        if is_available:
            print(f"Book {book_name} issued successfully ")
        else:
            print(f"Book {book_name} is not available ")
