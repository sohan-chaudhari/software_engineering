class BookService:
    def issue_book(self, book_name, is_available):
        if is_available:
            return True
        return False


class MessagePrinter:
    def print_message(self, book_name, status):
        if status:
            print(f"Book '{book_name}' issued successfully")
        else:
            print(f"Book '{book_name}' is not available")  
