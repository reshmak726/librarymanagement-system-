# student library

class library:
    def __init__(self,listofbooks):
        self.books = listofbooks
        
        
    def displayavailablebooks(self):
        print("****the books present in this library are:***** ")
        for book in self.books:
            
            print("\t"+book)

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. Please keep it safe and return on time mentioned!!")
            self.books.remove(bookname)
            return True

        else:
            print("sorry ! either book is isssued by someone else .or the book is not available please wait until the book is available")
            return False
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("thanks for returning this book! ")
class student:
    def __init__(self):
        self.booklist = []
    def requestbook(self):
        self.book = input("enter the name of the book you want to borrow..: ")
        return self.book

    def returnbook(self):
        self.book = input("enter the name of the book you want to return..: ")
        return self.book


if __name__ == "__main__":
    centralibrary =library(["cn","algorithms","maths","reference","pythonbooks"])
    student = student()
    # centralibrary.displayavailablebooks()
    while(True):
        welcomemsg = ''' ****welcome to library ***** 
        please choose an option:
        1.Listing all the books
        2.Request a book
        3. Return a book
        4. Exit the library

         '''
        print(welcomemsg)
        a = (int(input("enter a choice: ")))
        if a == 1:
            centralibrary.displayavailablebooks()

        elif a == 2:
            centralibrary.borrowbook(student.requestbook())

        elif a == 3:
            centralibrary.returnbook(student.returnbook())

        elif a == 4:
            print("thanks for using this library 😊 !!")
            exit()

