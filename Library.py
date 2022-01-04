import datetime


class Library:

    def __init__(self,BookCollection,Name):
        self.name = Name 
        self.bookCollection = BookCollection

    def displaybook(self):
        # Display the all books in our collection 
        print(self.bookCollection)

    def lend_books(self):
        lendRecord = open("lendRecord.txt","a+")
        print("The books in our collection...")
        for i in range(len(self.bookCollection)):
            print(f"{i+1}.{self.bookCollection[i]}")

        bookrequest = int(input())
        lendRecord.write(f"{self.bookCollection[bookrequest-1]} lended by {username} at {time}\n")
        Library_liveDict[username] = self.bookCollection[bookrequest -1]
        self.bookCollection.remove(self.bookCollection[bookrequest-1])
        print(self.bookCollection)

    def return_book(self):
        # ()
        book_returner = input(f"Okay ! Please enter your name here:\n:")
        if book_returner in Library_liveDict:
           print(f"Yes ! you have lended a {Library_liveDict[book_returner]} from us.\n so confirm to return it ?")
           confirm = int(input("0.Yes\n1.No\n"))
           if confirm == 0:
               self.bookCollection.append(Library_liveDict[book_returner])
               del Library_liveDict[book_returner]
               print(self.bookCollection)
           else:
               print("Something went wrong")
               

    def add_book(self):
        donater = input("Please Enter Your Name Here:\n")
        donatedBook = input("Please Enter the Name of book which you want to donate:\n")
        self.bookCollection.append(donatedBook)
        print(f"Thank you so much for donating a book.")
        print(self.bookCollection)



if __name__ == "__main__":
    time = datetime.datetime.now()
    booklist = []
    LibName = input("Enter Lirary Name:\n")
    NoOfBook = int(input("Enter here how many books you want to add in your library:\n"))
    for i in range(NoOfBook):
        booklist.insert(i, input(f"{i+1}.Enter The Book Name: "))

    User = Library(booklist,LibName)
    Library_liveDict= {}
    try:
        username = input("Enter Your Name Here:\n")
        
        while True:

            visit = open("VisitorRecord.txt","a+")
            print("-*-------Welcome To Library !-------*-")
            visit.write(f"The Visitor {username}--Visited {time}\n")
            print("1.Display to all Books\n2.Lend Book\n3.Return Book\n4.Donate a Book to library")
            
            user_input = int(input("Enter what you want to do:\n"))
            
            if user_input == 1:
                User.displaybook()
            elif user_input == 2:
                User.lend_books()
            elif user_input == 3:
                User.return_book()
            elif user_input == 4:
                User.add_book()
            else:
                print("Invalid input !")
            
            
          
    except Exception as Error:
        print("Something Wrong Input")
        __name__()


