#!/usr/bin/env python3
# Program Name: main.py
# Purpose: displays the menu and captures book/owner details.
# Author: prasanna
# Document:
# Logs:
# 08-Aug-2026 - prasanna - Creation date.
# 10-Aug-2026 - prasanna - Captured owner and book information.
# 11-Aug-2026 - prasanna - Added validation for year, title, room number, and edition;
# program exits with a message on invalid input.
# 12-Aug-2026 - prasanna - created a book list, added multiple entries one at a time, 
#                          displayed the total number of books by numbering.
# 15-Aug-2026 - prasanna - Added while loop, wired Add/View book branches,
#                          replaced exit() with continue for validation reasons.
from datetime import date
books = []          # books list

print("-" * 30)
print("HOSTEL LIBRARY BOOK SHARING")
print("-" * 30)
print("Welcome to the Hostel Library")
#while loop to choose actions repeatedly 
while True:
   print()     
   print("1. Add Book")
   print("2. View Books")
   print("3. Search Books")
   print("4. Borrow Book")
   print("5. Return Book")
   print("6. Exit")
   print()
   choice = input("Choose your Choice:").strip()
   print()
   if choice == "1":
      print ("1. Add Book")
      print("Add a New Book")
      print()
#user inputs
      owner_name = input("Owner Name: ").strip()
      room_number = int(input("Hostel Room Number: ").strip())
      title = input("Book Title: ").strip()
      author = input("Author: ").strip()
      category = input("Category: ").strip()
      edition = int(input("Edition: ").strip())
      year = int(input("Publication Year: ").strip())

   ## user input validation 
   #room number
      if room_number <= 0:
         print("Invalid Room number:cannot be lessthan or equal to 0")
         continue
      elif room_number > 500:
         print("Invalid Room number:must be in range 1 to 500")
         continue
      else:
         pass
   #book title
      if owner_name != "" and title != "" and author != "" and category != "":
         pass   
      else:
         print("No field can be left empty")
         print("Book cannot be added!")
         continue
   #edition
      if edition < 1:
         print("Invalid Edition: Please enter a positive integer")
         continue
      else:
         pass
   #year
      if year < 1900:
         print(f"Invalid year: please enter a year in between 1900 and {date.today().year}.")
         continue
      elif year > date.today().year:
         print(f"Invalid year: Please enter  a year in between 1900 and {date.today().year}.")
         continue
      else:
         pass
      print()
      print("Book Added")   # Displays book added
      print()
      books.append(title)   # To add more books
      print()
      print(f"Owner       : {owner_name}")     # To display what users had entered
      print(f"Room Number : {room_number}")
      print(f"Title       : {title}")
      print(f"Author      : {author}")
      print(f"Category    : {category}")
      print(f"Edition     : {edition}")
      print(f"Year        : {year}")
      print("-" * 20)

#under view books display book number with numbering and total no.of books
   elif choice == "2":
      print("2. View Books")
      for i, book in enumerate(books, start = 1):   # for loop
         print(f"{i}.{book}")                       # printing books added by numbering
         print()
      print(f"Total Books: {len(books)}")           # To display total numbers books added

   elif choice == "3":
      print("3. Search Books")
   elif choice == "4":
      print("4. Borrow Book")
   elif choice == "5":
      print("5. Return Book")
   elif choice == "6":
      False
      print("Exiting... Good bye!")
   else:
      print("Invalid choice! Please try again!")