from dataclasses import dataclass
import datetime
import asyncio

users = [
    {
       "user_id" : "U123",
       "name" : "John",
       "membership" : "premium" 
    },
    {
       "user_id" : "U456",
       "name" : "Jane",
       "membership" : "regular" 
    }
]

books = [
    {
        "book_id" : "B001",
        "title" : "Python Basics",
        "author" : "Alice",
        "copies_total" : 4,
        "copies_available" : 4
    },
    {
        "book_id" : "B002",
        "title" : "System Design",
        "author" : "Bob",
        "copies_total" : 2,
        "copies_available" : 0
    }
]

transactions = [
    {
        "transaction_id" : "T001",
        "book_id" : "B002",
        "user_id" : "U123",
        "borrowed_date" : "2025-09-15",
        "due_date" : "2025-10-06",
        "returned_date" : None,
        "fine_amount" : 0
    },
    {
        "transaction_id" : "T003",
        "book_id" : "B001",
        "user_id" : "U456",
        "borrowed_date" : "2025-10-01",
        "due_date" : "2025-10-22",
        "returned_date" : "2025-10-23",
        "fine_amount" : 1
    },
    {
        "transaction_id" : "T002",
        "book_id" : "B001",
        "user_id" : "U456",
        "borrowed_date" : "2025-10-01",
        "due_date" : "2025-10-22",
        "returned_date" : "2025-11-05",
        "fine_amount" : 14.0
    },
    
]



@dataclass
class User():
    user_id : str
    name : str | None = None
    membership : str | None = None

    async def user_info(self):
        detail = {}
        for user in users:
            if user["user_id"] == self.user_id:
                    detail = user
        return detail

    async def verify_user(self):
        user_exist = False
        for user in users:
            if user["user_id"] == self.user_id:
                user_exist = True
        return user_exist

    async def verify_user_return_book(self):
        total_borrowed_book = 0
        for transaction in transactions:
            if transaction["user_id"] == self.user_id and transaction["returned_date"] != None:
                total_borrowed_book = total_borrowed_book + 1

        return total_borrowed_book
    
    async def user_history(self):
        total_overdue = 0
        total_fines = 0
        total_borrowed = 0
        currently_borrowed = 0
        for transaction in transactions:
            if transaction["user_id"] == self.user_id:
                total_borrowed = total_borrowed + 1
                if transaction["fine_amount"] != 0:
                    total_overdue = total_overdue + 1
                    total_fines = total_fines + transaction["fine_amount"]

                if transaction["returned_date"] == None:
                    currently_borrowed = currently_borrowed + 1
        return {
            "Total Overdue" : total_overdue,
            "Total fines" : total_fines,
            "Total Borrowed" : total_borrowed,
            "Currently Borrowed" : currently_borrowed
        }

                


 

@dataclass
class Books(User):
    book_id : str | None = None
    user_id : str | None = None
    transaction_id : str | None = None
    title : str | None = None
    author : str | None = None
    copies_total : int | None = None
    copies_available : int | None = None

    async def update_book(self, inc = False,dcr = False):
        for book in books:
            if book["book_id"] == self.book_id:
                if dcr:
                    book["copies_available"] = book["copies_available"] - 1
                if inc:
                    book["copies_available"] = book["copies_available"] + 1

    # Sort book by overdue books
    @staticmethod
    async def overdue_books():
        overdue_books = {}
        for transaction in transactions:
            if transaction["returned_date"] != None:
                returned_date = datetime.date.fromisoformat(transaction["returned_date"])
                due_date = datetime.date.fromisoformat(transaction["due_date"])
                overdue_books[(returned_date-due_date).days] = transaction
        sorted_overdue_book = [value for key,value in sorted(overdue_books.items(),reverse=True)]
        print(sorted_overdue_book)

    # Sort Book by Fine amount
    @staticmethod
    async def fine_amount():
        fined_books = {}
        for transaction in transactions:
            if transaction["fine_amount"] != 0:
                fined_books[transaction["fine_amount"]] = transaction
        sorted_fined_books = [value for key,value in sorted(fined_books.items(),reverse=True)]
        print(sorted_fined_books)


    # sort Book by Transaction ID
    @staticmethod
    async def sort_by_transaction_id():
        transaction_book = {}
        for transaction in transactions:
            transaction_book[int(transaction["transaction_id"][1:4])] = transaction
        sort_by_transaction_book = [value for key,value in sorted(transaction_book.items())]
        print(sort_by_transaction_book)


    @staticmethod
    async def book_info():
        return books

    async def most_popular_books(self, n=5):
        book_counts = {}

        for transaction in transactions:
            book_id = transaction["book_id"]
            book_counts[book_id] = book_counts.get(book_id, 0) + 1

        sorted_books = dict(
            sorted(book_counts.items(), key=lambda item: item[1], reverse=True)
        )

        detail_data = []
        already_in_dict = set()

        for transaction in transactions:
            book_id = transaction["book_id"]

            if book_id in sorted_books and book_id not in already_in_dict:
                detail = transaction.copy()
                detail["counts"] = sorted_books[book_id]
                detail_data.append(detail)
                already_in_dict.add(book_id)

            if len(detail_data) >= n:
                break

        return detail_data
    
    @staticmethod
    async def search_book(search: str):
        searched_book = []
        search = search.lower()

        for book in books:
            if book["copies_available"] > 0 and (
                search in book["title"].lower()
                or search in book["author"].lower()
            ):
                searched_book.append(book)
                # print(book)

        return searched_book


@dataclass
class Transactions(Books):
    transaction_id : str | None = None
    book_id : str| None = None
    user_id : str | None = None
    borrowed_date : datetime.date | None = None
    due_date : datetime.date | None = None
    returned_date : datetime.date | None = None
    fine_amount : int | None = None

    @staticmethod
    async def all_transactions():
        return transactions 
    
    async def transaction_info(self):
        t_info = {}

        for transaction in transactions:
            if transaction["transaction_id"] == self.transaction_id:
                t_info = transaction
        return t_info
    
    async def verify_transaction(self):
        borrowed_book_exist = False
        for borrowed_books in transactions:
            if borrowed_books['transaction_id'] == self.transaction_id and borrowed_books["book_id"] == self.book_id and borrowed_books["user_id"] == self.user_id:
                borrowed_book_exist = True

        return borrowed_book_exist 
    

    async def update_transaction(self,returned_date, fine = None):
        for borrowed_books in transactions:
            if borrowed_books['transaction_id'] == self.transaction_id and borrowed_books["book_id"] == self.book_id and borrowed_books["user_id"] == self.user_id:
                borrowed_books["returned_date"] = returned_date
                if fine:
                    borrowed_books["fine_amount"] = fine



    
    async def borrow_book(self):
        user_exist =await self.verify_user()
        total_borrowed_book =await self.verify_user_return_book()
        book_exist = False
        if user_exist and total_borrowed_book < 3:
            for book in books:
                if book["book_id"] == self.book_id and book["copies_available"] > 0:
                    book_exist = True
        if book_exist:
            await self.update_book(dcr=True)

            total_transaction = len(transactions) + 1
            detail = {
                "transaction_id" : "T00"+str(total_transaction),
                "book_id": self.book_id,
                "user_id" : self.user_id,
                "borrowed_date" : datetime.datetime.now().strftime('%Y-%m-%d'),
                "due_date" : (datetime.datetime.now() + datetime.timedelta(days=21)).strftime('%Y-%m-%d'),
                "returned_date" : None,
                "fine_amount" : 0
            }
            transactions.append(detail)
            return "Book borrowed"
        else:
            return "Failed to Borrow Book"
        
    async def return_books(self):
        borrowed_book_exist = await self.verify_transaction()
        dates = datetime.datetime.now()
        totalfine = 0
        if borrowed_book_exist:
            user_detail = await self.user_info()
            transaction_detail = await self.transaction_info()
            returned_date = datetime.date.fromisoformat(transaction_detail["due_date"])
            number_of_days = (dates.date() - returned_date).days
            if user_detail["membership"] == "Premium".lower():
                if number_of_days < 0:
                    totalfine = 0
                else:
                    totalfine = number_of_days - 7
            else:
                totalfine = number_of_days
            await self.update_transaction((dates.date()).strftime('%Y-%m-%d'),fine=totalfine)
            await self.update_book(inc=True)
        return f"Book Returned with fine:{totalfine}"

async def main():
    # task1 = asyncio.create_task(Books.book_info())
    # task2 = asyncio.create_task(Transactions.all_transactions())
    # result1 = await task1
    # result2 = await task2
    # print("Book Infos",result1)
    # print("Transaction Infos",result2)

    # borrow_book1 = Transactions(user_id="U456",book_id="B002")
    # print(await borrow_book1.borrow_book())

    await Books.sort_by_transaction_id()
    # print(await all_transactions())
    # transaction1 = Transactions()
    # print(await transaction1.most_popular_books(2))
    # print(await transaction1.return_books())
    # print(await all_transactions())
    # print("Books available:",await book_info())
    # print(await Books.search_book("alice"))

# if __name__ == "__main__":
asyncio.run(main())