# Library management system

# Write a Library class with no_of_books and books as two instace variables.
# Write a prog to create a library from this Library class and show how you can print all books, add a book and get no. of books.
# Show that your prog doesnt accept books after prog is stopped



class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books = len(self.books)

    def show_info(self):
        print(f"Total number of books, {self.no_of_books}")




while True:
    print("1.Add a book\n2.Show book count\n3. Quit")
    p = int(input("Enter choice"))
    if(p==1):
        while True:
            try:
                user = int(input("Enter how many books you want to add"))
                if user>0:
                    break
            except Exception as e:
                print("Enter only +ve digits")

        l1 = Library()
        i = 0 
        while(i < user):     
            book_ip = input("Enter name of books")
            l1.add_book(book_ip)
            i += 1

    if(p==2):
        l1.show_info()


    if(p==3):
        break


# 1.Add a book
# 2.Show book count
# 3. Quit
# Enter choice1
# Enter how many books you want to add3
# Enter name of booksasd
# Enter name of booksklj
# Enter name of booksrty
# 1.Add a book
# 2.Show book count
# 3. Quit
# Enter choice2
# Total number of books, 3
# 1.Add a book
# 2.Show book count
# 3. Quit
# Enter choice3
# PS H:\100 Days of Python\Day 51-60\Day51> 