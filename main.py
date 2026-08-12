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

from datetime import date

print("-" * 30)
print("HOSTEL LIBRARY BOOK SHARING")
print("-" * 30)

print()
print("Welcome to the Hostel Library")
print()
print("1. Add Book")
print("2. View Books")
print("3. Search Books")
print("4. Borrow Book")
print("5. Return Book")
print("6. Exit")

print()
print("Add a New Book")
print()

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
   exit()
elif room_number > 500:
   print("Invalid Room number:must be in range 1 to 500")
   exit()
else:
   pass
#book title
if owner_name != "" and title != "" and author != "" and category != "":
    pass   
else:
    print("No field can be left empty")
    print("Book cannot be added!")
    exit()
#edition
if edition < 1:
  print("Invalid Edition: Please enter a positive integer")
  exit()
else:
   pass
#year
if year < 1900:
    print(f"Invalid year: please enter a year in between 1900 and {date.today().year}.")
    exit()
elif year > date.today().year:
    print(f"Invalid year: Please enter  a year in between 1900 and {date.today().year}.")
    exit()
else:
  pass

print()
print("Book Added")
print(f"Owner       : {owner_name}")
print(f"Room Number : {room_number}")
print(f"Title       : {title}")
print(f"Author      : {author}")
print(f"Category    : {category}")
print(f"Edition     : {edition}")
print(f"Year        : {year}")
print("-" * 20)