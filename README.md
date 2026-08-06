Project Title
Hostel Library Book Sharing System
Project Description

Students living in a hostel often own books that others would like to borrow. Instead of purchasing duplicate books, they voluntarily share their books through a common system.

The application will:

Maintain a catalog of books owned by hostel students.
Track who owns each book.
Allow students to borrow available books.
Enforce a maximum borrowing period of 7 days.
Maintain a waiting queue for popular books.
Notify the next student in the queue when a book is returned.
Generate useful reports such as:
Total books in the hostel
Books by owner
Duplicate (common) titles
Most requested books
Overdue books
Borrowing history
Learning Objectives

By the end of the project, students will understand:

Variables and user input
Conditions and loops
Lists, tuples, dictionaries, and sets
Functions and modular programming
Exception handling
Debugging techniques
Logging
Object-Oriented Programming
JSON file handling
Date and time operations
Queue data structures
Clean project organization
Suggested Project Structure
HostelLibrary/

│
├── main.py
├── models.py
├── library.py
├── borrow.py
├── reports.py
├── queue_manager.py
├── utils.py
├── logger.py
├── data.json
├── borrow_history.json
├── logs.txt
└── README.md
WEEK 1 – Python Fundamentals
Day 1 – Understanding the Problem
Objective

Understand how the Hostel Library Sharing System will work.

Theory

Discuss:

Why students share books.
Roles:
Owner
Borrower
Library System
Rules:
A book belongs to one owner.
A student may borrow only available books.
Books must be returned within seven days.
If unavailable, a waiting queue is created.
Practical Tasks

Create the project folder and display a welcome screen with a placeholder menu.

Learning Outcome

Understand project requirements and basic program structure.

Day 2 – User Input
Objective

Capture owner and book information.

Topics
Variables
Strings
Integers
Input
Practical Tasks

Allow entry of:

Owner Name
Hostel Room Number
Book Title
Author
Category
Edition
Publication Year

Display the information in a neat format.

Challenge

Validate that mandatory fields are not left blank.

Day 3 – Conditions
Objective

Validate entered data.

Topics
if
elif
else
Practical Tasks

Ensure:

Publication year is reasonable.
Book title is not empty.
Room number is valid.
Edition is positive.

Reject invalid data with helpful messages.

Day 4 – Lists
Objective

Store multiple books.

Practical Tasks

Create a list to hold books and add multiple entries. Display all books with numbering.

Challenge

Show the total number of books entered.

Day 5 – Loops
Objective

Build a repeating menu.

Practical Tasks

Create a while loop that lets the user repeatedly choose actions until they exit.

Day 6 – Search
Objective

Find books.

Practical Tasks

Search by:

Title
Author
Owner

Display matching books.

Day 7 – Weekly Review

Integrate:

Add Book
View Books
Search Books
Exit
WEEK 2 – Collections & Functions
Day 8 – Dictionaries

Represent each book as a dictionary containing:

Book ID
Title
Author
Owner
Room Number
Availability
Borrower
Due Date
Day 9 – Nested Dictionaries

Store all books using Book ID as the key. Enable efficient searching and updating.

Day 10 – Sets (Finding Common Books)
Objective

Identify duplicate titles.

Practical Tasks

Use sets and counting logic to:

Find unique titles.
Find titles owned by multiple students.
Display how many copies of each common title exist.
Example Report
Python Crash Course — 4 copies
Clean Code — 2 copies
Atomic Habits — 5 copies
Day 11 – Functions

Create reusable functions such as:

add_book()
view_books()
search_books()
books_by_owner()
Day 12 – Reports

Generate reports for:

Total books
Books by owner
Books by category
Available books
Borrowed books
Day 13 – Code Cleanup

Refactor repeated code, improve naming, and add documentation.

Day 14 – Weekly Review

Complete a stable version supporting book management and reporting.

WEEK 3 – Borrowing System
Day 15 – Borrowing Books
Objective

Allow students to borrow available books.

Practical Tasks

Record:

Borrower Name
Borrow Date
Due Date (7 days later)

Mark the book as unavailable.

Day 16 – Returning Books
Objective

Handle returns.

Practical Tasks

When a book is returned:

Mark it available.
Record the return date.
Update borrowing history.
Day 17 – Queue System
Objective

Manage waiting requests.

Topics
Queue data structure
FIFO (First In, First Out)
Practical Tasks

If a requested book is unavailable:

Add the requester to the waiting queue.
Show their position in the queue.
Day 18 – Queue Processing
Objective

Automatically assign returned books.

Practical Tasks

When a book is returned:

Check the waiting queue.
Assign the book to the next student.
Remove them from the queue.
Update due dates.
Day 19 – Date Handling
Topics
datetime
timedelta
Practical Tasks

Calculate:

Borrow date
Due date
Remaining days

Highlight overdue books.

Day 20 – Reports

Generate:

Overdue books
Most requested books
Longest waiting queue
Current borrowers
Day 21 – Weekly Review

Test all borrowing, returning, queue, and reporting features.

WEEK 4 – Professional Python
Day 22 – Modules

Split the project into:

library.py
borrow.py
reports.py
queue_manager.py
utils.py
Day 23 – Exception Handling

Handle:

Invalid Book ID
Missing book
Invalid dates
Empty queue
Duplicate entries

Create custom exceptions such as:

BookNotAvailableError
BookNotFoundError
Day 24 – Debugging

Use:

Print debugging
VS Code debugger
Breakpoints
Variable inspection

Introduce intentional bugs for practice.

Day 25 – Logging

Use the logging module to record:

Book added
Book borrowed
Book returned
Queue joined
Queue processed
Errors
Day 26 – Object-Oriented Programming

Create classes:

Book
Student
Library
BorrowTransaction

Move existing logic into class methods.

Day 27 – Advanced OOP

Introduce:

Encapsulation for book details.
Inheritance (e.g., ReferenceBook and BorrowableBook).
Polymorphism for displaying different types of books.
Day 28 – JSON Storage

Save and load:

Books
Students
Borrow history
Waiting queues

Automatically restore data when the program starts.

Day 29 – Advanced Reports

Create reports such as:

Total books in hostel
Books owned by each student
Top 10 owners with the largest collections
Most borrowed books
Most requested books
Common titles across the hostel
Average borrowing duration
Students with overdue books
Books never borrowed
Borrowing activity by category
Day 30 – Final Testing & Documentation
Final Integration

Perform end-to-end testing of all features, verify queue processing, validate the 7-day borrowing rule, and ensure data is correctly saved and restored.

Documentation

Prepare a README.md explaining:

Project overview
Features
Installation
How to run the application
Folder structure
Example usage
Future enhancements
Stretch Goals (Optional)

If time permits, students can add:

Email or in-app notifications when a queued book becomes available.
Book ratings and reviews.
QR codes or barcode-based book identification.
Fine calculation for overdue returns.
Reservation cancellation.
Admin and student login roles.
Search by ISBN, author, or category.
Statistics dashboard showing borrowing trends.
Final Features Checklist

By the end of the project, the application should support:

✅ Register book owners and their collections
✅ Add, update, search, and remove books
✅ View all books owned by a specific student
✅ Count the total number of books in the hostel
✅ Identify common (duplicate) book titles shared by multiple owners
✅ Search books by title, author, category, or owner
✅ Borrow available books
✅ Enforce a maximum borrowing period of 7 days
✅ Return books and update availability
✅ Maintain a FIFO waiting queue for unavailable books
✅ Automatically assign returned books to the next student in the queue
✅ Track borrowing history
✅ Generate comprehensive reports
✅ Handle errors gracefully with exceptions
✅ Log important application events
✅ Organize the project into modules
✅ Use Object-Oriented Programming for a clean and scalable design
✅ Persist all data using JSON files

This project closely mirrors a real-world library lending system while remaining accessible to beginners. It progressively introduces Python fundamentals and software engineering practices through meaningful, practical tasks.
