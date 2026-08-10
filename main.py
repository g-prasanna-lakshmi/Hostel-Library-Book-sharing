#!/usr/bin/env python3

# Program Name: Hostel Library Book Sharing
# Purpose: displays the menu and captures book/owner details.
# Author: prasanna
# Document: main.py
# Logs:
# 08-Aug-2026 - prasanna - Creation date.
# 10-Aug-2026 - prasanna - Captured owner and book information.

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
room_number = input("Hostel Room Number: ").strip()
title = input("Book Title: ").strip()
author =input("Author: ").strip()
category = input("Category: ").strip()
edition = input("Edition: ").strip()
year = input("Publication Year: ").strip()

print()
print("Book Added")
print(f"Owner       : {owner_name}")
print(f"Roon Number : {room_number}")
print(f"Title       : {title}")
print(f"Author      : {author}")
print(f"Category    : {category}")
print(f"Edition     : {edition}")
print(f"Year        : {year}")
print("-" * 20)