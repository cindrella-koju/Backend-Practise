import datetime

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
        "borrowed_date" :datetime.date.fromisoformat("2025-09-15"),
        "due_date" : datetime.date.fromisoformat("2025-10-06"),
        "returned_date" : None,
        "fine_amount" : 0
    },
    {
        "transaction_id" : "T003",
        "book_id" : "B001",
        "user_id" : "U456",
        "borrowed_date" : datetime.date.fromisoformat("2025-10-01"),
        "due_date" : datetime.date.fromisoformat("2025-10-22"),
        "returned_date" : datetime.date.fromisoformat("2025-10-23"),
        "fine_amount" : 1
    },
    {
        "transaction_id" : "T002",
        "book_id" : "B001",
        "user_id" : "U456",
        "borrowed_date" : datetime.date.fromisoformat("2025-10-01"),
        "due_date" : datetime.date.fromisoformat("2025-10-22"),
        "returned_date" : datetime.date.fromisoformat("2025-11-05"),
        "fine_amount" : 14.0
    },
    
]