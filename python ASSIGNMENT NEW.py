while True:
    try:
        age = int(input("What is your age? "))
        print(f"Your age is {age}")
        break
    except ValueError:
        print("That's not a valid number. Please try again.")

        # QUESTION 2
        fruits = ["Apple", "Mango", "Banana", "Oranges", "Grapefruit"]
        with open("fruits.txt", "w") as file:
            for fruit in fruits:
                file.write(fruit + "|n" )
                with open("fruits.txt", "r") :
                    contents =file.readlines()
                    for line in contents:
                        print(line.strip())


             #QUESTION 3
students = {"Charles": 78,
             "Carter": 85,
             "Malvin": 67,
             "Denver": 92,
             "Nova":88}
print ("ALL students and marks:")
for name, mark in students.items():
     print(f"{name}: {mark}")
     top_student = max(students, key=students.get)
     print(f"\tTop student: {top_student}")

    #QUESTION 3ii
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        pass

    def display(self):
     print(f'Title: {self.title}), Author: {self.author}, Price: ${self.price:.2f}')
book1 = Book("1984", "George Orwell", 8.99)
book1.display_details()
book2 = Book("Dune", "Frank Herbert", 10.50)
print()
book2.display()

    #QUESTION 4
from datetime import datetime
from collections import Counter

def find_peak_usage(timestamps):
    # Step 1: extract just the hour (0-23) from each timestamp
    hours = [datetime.fromisoformat(ts).hour for ts in timestamps]
    # Step 2: count how many logins happened in each hour
    counts = Counter(hours)
    # Step 3: find the hour with the highest count;
    # on a tie, prefer the smaller (earlier) hour
    peak_hour = max(range(24), key=lambda h: (counts.get(h, 0), -h))
    return peak_hour

    #Example test
logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:02",
    "2026-08-04T13:10:00",
    "2026-08-04T13:59:59",
    "2026-08-04T13:30:00"
    ]
print(find_peak_usage(logs))





















