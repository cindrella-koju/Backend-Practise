import time
import asyncio

""" Synchronous Transactions """
books = [
    {
        "name": "November 9",
        "writer" : "Coolen Hoover",
        "copies" : 3
    },
    {
        "name" : "One Piece Manga",
        "writer" : "ODA",
        "copies" : 2
    }
]


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Name",self.name)

# borrowed_book = []
# returned_book = []


# class Library(Person):
#     def __init__(self,book_name,book_writer,name):
#         super().__init__(name)
#         self.book_name = book_name
#         self.book_writer = book_writer

#     def borrow_book(self):
#         book_available = False
#         for book in books:
#             if self.book_name == book['name'] and self.book_writer == book["writer"] and book["copies"] > 0:
#                 book["copies"] = book["copies"] -1
#                 book_available = True

#         if book_available == False:
#             time.sleep(1)
#             return "Book not available"
#         else:
#             detail = {
#                 "user" : self.name,
#                 "book_name": self.book_name,
#                 "book_writer": self.book_writer
#             }
#             time.sleep(2)
#             borrowed_book.append(detail)
#             return f"{self.name} Borrowed the book {self.book_name}"

# def display_borrowed_book():
#     for data in borrowed_book:
#         print(data)

# def display_book():
#     for book in books:
#         print(book['name'])

# def main():
#     starttime = time.time()
#     obj1 = Library("One Piece Manga","ODA","Cindrella")
#     print(obj1.borrow_book())
#     obj2 = Library("One Piece Manga","ODA","Cindrella")
#     print(obj2.borrow_book())
#     obj3 = Library("One Piece Manga","ODA","Cindrella")
#     print(obj3.borrow_book())
#     print("Transaction completed at:",time.time()-starttime)

class Person:
    def __init__(self, name):
        self.name = name

    async def info(self):
        print("Name",self.name)

borrowed_book = []
returned_book = []


class Library(Person):
    def __init__(self,book_name,book_writer,name):
        super().__init__(name)
        self.book_name = book_name
        self.book_writer = book_writer

    async def borrow_book(self):
        book_available = False
        for book in books:
            if self.book_name == book['name'] and self.book_writer == book["writer"] and book["copies"] > 0:
                book["copies"] = book["copies"] -1
                book_available = True

        if book_available == False:
            await asyncio.sleep(1)
            return "Book not available"
        else:
            detail = {
                "user" : self.name,
                "book_name": self.book_name,
                "book_writer": self.book_writer
            }
            await asyncio.sleep(2)
            borrowed_book.append(detail)
            return f"{self.name} Borrowed the book {self.book_name}"

def display_borrowed_book():
    for data in borrowed_book:
        print(data)

def display_book():
    for book in books:
        print(book['name'])

async def main():
    starttime = time.time()
    async with asyncio.TaskGroup() as tg:
        obj1 = Library("One Piece Manga","ODA","Cindrella")
        task1 = tg.create_task(obj1.borrow_book())
        obj2 = Library("One Piece Manga","ODA","Cindrella")
        task2 = tg.create_task(obj2.borrow_book())
        obj3 = Library("One Piece Manga","ODA","Cindrella")
        task3 = tg.create_task(obj3.borrow_book())


    print(task1.result(),task2.result(),task3.result())
        
    print("Transaction completed at:",time.time()-starttime)

if __name__ == "__main__":
    asyncio.run(main())