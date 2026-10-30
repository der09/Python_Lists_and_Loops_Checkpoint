# Name:Diane Hsieh
# Period: AM 

# ============================================================
# Python Skills Check — LISTS & LOOPS
# CHALLENGE VERSION — 40 TASKS
# ============================================================
# DIRECTIONS:
# - Create a repository, clone it, and add this file.
# - Complete each task UNDER its directions.
# - Do not delete the directions.
# - Use ONLY concepts learned in class, except for 'in' and 'not in'.
#   You must research these two new operators independently in Section 5.
# - Use the EXACT variable and function names provided.
# - The entire file must run without errors.
# - Do not hard-code results Python should calculate.
# - Unless a task says otherwise, do NOT use sum(), min(), max(),
#   sorted(), sort(), list comprehensions, sets, or dictionaries.
# - For functions, RETURN values when instructed; do not just print.
# - Test edge cases and change the starting values to check your logic.
# - Tasks that ask for input() may be tested individually.

# ============================================================
# SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# ============================================================

# TASK 1:
# Create a list named scores containing 85, 92, 78, 96, 88.
# Print the entire list and its length using len().
print()
print("Task 1:")
print()

scores = [85, 92, 78, 96, 88]
print (scores)
print (len(scores))

# TASK 2:

# Using scores from Task 1, print the FIRST, THIRD, and LAST
# elements on separate lines. Use indexes, not hard-coded values.
print()
print("Task 2:")
print()

print(scores[0])
print(scores[2])
print(scores[len(scores) - 1])

# TASK 3:
# Change the third element of scores to 100.
# Print the updated list. Do not create a replacement list.
print()
print("Task 3:")
print()

scores[2] = 100
print(scores)

# TASK 4:
# Create games = ["Minecraft", "Roblox", "Fortnite"].
# Append "Valorant" and insert "Rocket League" at index 1.
# Print games. Check the order carefully.
print()
print("Task 4:")
print()

games = ["Minecraft", "Roblox", "Fortnite"]
games.append("Valorant")
games.insert(1, "Rocket League")
print(games)

# TASK 5:
# Using games from Task 4, remove "Roblox" with remove().
# Then pop the FIRST item into a variable named removed_game.
# Print removed_game and the remaining games list.

print()
print("Task 5:")
print()

games.remove("Roblox")
removed_game = games.pop(0)
print(removed_game)
print(games)

# TASK 6:
# Create colors = ["red", "blue", "green", "yellow", "purple"].
# Store the index of "green" in green_index using index().
# Print green_index. Then replace "yellow" with "orange".
# Print the new list.

print() 
print("Task 6:")
print()

colors = ["red", "blue", "green", "yellow", "purple"]
green_index = colors.index("green")
print(green_index)

colors[3] = "orange"
print(colors)

# ============================================================
# SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# ============================================================

# TASK 7:
# Use a for loop with range() to print numbers 1 through 20,
# INCLUDING 20. Do not manually print the numbers.

print()
print("Task 7:")
print()

for i in range(1, 21): 
    print(i)

# TASK 8:
# Use a for loop with range() to print 30, 27, 24, ... 0.
# IMPORTANT: The zero must be included.

print()
print("Task 8:")
print()

for i in range(30, -1, -3):
    print(i)

# TASK 9:
# Use a for loop to print all EVEN numbers from 1 to 50.
# You MUST use an if statement and the % operator inside the loop.

print()
print("Task 9:")
print()

for i in range(1, 51): 
    if i % 2 == 0: 
        print(i)

# TASK 10:
# Create number = 7.
# Print its multiplication table from 1 through 12 using a for loop.
# Example line: 7 x 3 = 21
# Your code must also work if number changes.

print()
print("Task 10:")
print()

number = 7 
for i in range(1, 13): 
    print(number, "x", i, "=", (number * i))

# TASK 11:
# Create students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"].
# Use a for loop to print "Student: " followed by each name.
# Do NOT write five separate print statements.

print()
print("Task 11:")
print()

students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
for i in students: 
    print("Student: " + i)
    
# TASK 12:
# Using students, print a NUMBERED roster:
# 1. Alex
# 2. Jordan
# ...
# 5. Casey
# Use range(len(students)) OR enumerate().

print()
print("Task 12:")
print()

for i, name in enumerate(students, start=1):
    print(f"{i}. {name}")

# ============================================================
# SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# ============================================================

# TASK 13:
# Create countdown = 10.
# Use a while loop to print from countdown down to 0.
# Then print "Blast off!". Avoid an infinite loop.

print()
print("Task 13:")
print()

countdown = 10 
while countdown >= 0: 
    print(countdown)
    countdown = countdown - 1 
print("Blast off!")

# TASK 14:
# Create password = "Python123".
# Keep asking the user for a password until it matches.
# Print "Access granted" exactly once after a correct entry.

print()
print("Task 14:")
print()

password = "Python123"
question = input("Enter password: ")
while question != "Python123": 
    question = input("Enter password: ")

print("Access granted")

# TASK 15:
# Ask the user for an integer between 1 and 10 INCLUSIVE.
# Keep asking while the value is invalid.
# After a valid entry, print "Valid number".
# Test 0, 1, 10, and 11.

print()
print("Task 15:")
print()

integer = int(input("Enter an integer between 1 and 10: "))
while integer > 10 or integer < 1: 
    integer= int(input("Enter an integer between 1 and 10: "))
print("Valid number")

# TASK 16:
# Create total = 0.
# Repeatedly ask for an integer. Add each nonzero entry to total.
# Stop when the user enters 0, then print total.
# Example inputs: 5, 8, -2, 0 -> Total: 11.

print()
print("Task 16:")
print()

total = 0
integer = int(input("Enter an integer: "))
while integer != 0: 
    total = total + integer
    integer = int(input("Enter an integer:"))
print("Total:",total)


# TASK 17:
# Create secret = "robot" and attempts = 3.
# Ask the user to guess secret, allowing AT MOST 3 guesses.
# Print "Correct" if guessed in time; otherwise "Out of attempts".
# Make sure a correct guess does NOT print both messages.

print()
print("Task 17:")
print()

secret = "robot"
attempts = 3

while attempts > 0: 
    guess = input("Guess the secret: ")

    if guess == secret: 
        print("Correct")
        break
    else: 
        attempts = attempts - 1 

if attempts == 0: 
    print("Out of attempts")

# TASK 18:
# Make a while-loop menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit
# Repeat until the user enters 3. Handle invalid choices.
# Print "Goodbye" only when option 2 is selected.

print()
print("Task 18:")
print()


choice = int(input("Choose 1, 2, or 3: "))
if choice > 3 or choice < 1: 
    print("Invalid choice")
    choice = int(input("Choose 1, 2, or 3:"))
elif 1 <= choice <= 3: 
    while choice != 3: 
        if choice == 2: 
            print("Goodbye")
            print("1. Say Hello")
            print("2. Say Goodbye")
            print("3. Exit")
            print()
        elif choice == 1: 
            print("Hello")
            print("1. Say Hello")
            print("2. Say Goodbye")
            print("3. Exit")
            print()
        choice = int(input("Choose 1, 2, or 3:"))

# ============================================================
# SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# ============================================================

# TASK 19:
# Create numbers = [4, 8, 15, 16, 23, 42].
# Use a for loop to calculate and print their total.
# Do NOT use sum().

print()
print("Task 19:")
print()

total = 0
numbers = [4, 8, 15, 16, 23, 42]
for i in numbers: 
    total = total + i 
print(total)

# TASK 20:
# Create grades = [90, 85, 78, 92, 88].
# Use a loop and len() to calculate the average.
# Print the average. Do NOT use sum().

print()
print("Task 20:")
print()

total = 0 
grades = [90, 85, 78, 92, 88]
for i in grades: 
    total = total + i 
average = total/len(grades)
print(average)

# TASK 21:
# Create numbers = [3, 8, 12, 7, 15, 20, 24, 9].
# Use ONE loop to count even and odd values separately.
# Print "Even: [count]" and "Odd: [count]".

print()
print("Task 21:")
print()

even = 0 
odd = 0
numbers = [3, 8, 12, 7, 15, 20, 24, 9]
for i in numbers: 
    if i % 2 == 0: 
        even += 1 
    else: 
        odd += 1


print("Even:", even)
print("Odd:", odd)

# TASK 22:
# Create numbers = [-14, -67, -23, -89, -45].
# Use a loop to find and print the HIGHEST number.
# Do NOT use max() or sorting.
# IMPORTANT: Starting your answer at 0 gives a wrong result.

print()
print("Task 22:")
print()

numbers = [-14, -67, -23, -89, -45]
highest = numbers[0]
for i in numbers:
    if i > highest: 
        highest = i 
print("Highest number:", highest)


# TASK 23:
# Create numbers = [14, 67, 23, 89, 45, 12].
# Use a loop to find and print the LOWEST number.
# Do NOT use min() or sorting.
# Your logic must also work with all-negative numbers.

print()
print("Task 23:")
print()

numbers = [14, 67, 23, 89, 45, 12]
lowest = numbers[0]
for i in numbers: 
    if i < lowest: 
        lowest = i 
print("Lowest number:", lowest)

# TASK 24:
# Create numbers = [5, 2, 5, 8, 5, 3, 2, 5].
# Create target = 5.
# Use a loop to count how often target appears; print the count.
# Do NOT use count(). It must work if target changes.

print()
print("Task 24:")
print()

numbers = [5, 2, 5, 8, 5, 3, 2, 5]
target = 5 
count = 0 
for i in numbers: 
    if i == target: 
        count += 1 
print(count)

# ============================================================
# SECTION 5 — IN / NOT IN (TASKS 25–30)
# ============================================================
# INDEPENDENT RESEARCH REQUIRED:
# We have NOT covered 'in' and 'not in' in class. Before starting
# Tasks 25–30, research both operators on your own using reliable
# Python learning resources or the official Python documentation.
# Learn what each operator does, how it works with lists, and how
# to use it inside if statements and while loops.
# Write a short comment in your code explaining the difference
# between 'in' and 'not in' in your own words.
# The examples below are starting hints, NOT a substitute for research.
#
# NEW CONCEPT:
# 'in' checks whether a value is in a list.
# Example: "apple" in ["apple", "banana"] evaluates to True.
# 'not in' checks whether a value is missing.
# Example: "grape" not in ["apple", "banana"] evaluates to True.
# These expressions are useful in if statements and while loops.

# "in" checks if the value exists in the list 
# "not in" checks if the value does not exist in the list 

# TASK 25:
# Create foods = ["pizza", "burger", "tacos", "sushi", "pasta"].
# Ask the user to enter a food.
# Use 'in' to print "Available" or "Not available".
# Do NOT use index() to search.

print()
print("Task 25:")
print()

foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
choice = input("Enter a food: ")
if choice in foods: 
    print("Available")
else: 
    print("Not available")

# TASK 26:
# Create supplies = ["pencil", "notebook", "eraser", "backpack"].
# Ask the user for an item.
# Use 'not in' to print "Need to buy" if it is missing,
# otherwise print "Already have it".

print()
print("Task 26:")
print()

supplies = ["pencil", "notebook", "eraser", "backpack"]
item = input("Enter an item: ").strip()
if item not in supplies: 
    print("Need to buy")
else: 
    print("Already have it")

# TASK 27:
# Create usernames = ["alex123", "gamer99", "pythonpro"].
# Ask the user to enter a new username.
# If it is already in the list, print "Username taken".
# Otherwise append it and print the updated list.
# Do not allow duplicates.

print()
print("Task 27:")
print()

usernames = ["alex123", "gamer99", "pythonpro"]
username = input("Enter a new username: ")
if username in usernames: 
    print("Username taken")
else: 
    usernames.append(username)
    print(usernames)

# TASK 28:
# Modify the idea from Task 27 using a NEW list named accounts.
# Start with accounts = ["admin", "guest"].
# Use a while loop to keep asking until the entered name
# is NOT in accounts. Append the accepted name and print accounts.
# REQUIREMENT: Use 'not in' in your solution.

print()
print("Task 28:")
print()

accounts = ["admin", "guest"]
name = input("Input name: ")
while name in accounts: 
    name = input("Input name: ")
accounts.append(name)
print(accounts)

# TASK 29:
# Create secret_words = ["dragon", "robot", "python", "galaxy"].
# Keep asking the user for a word UNTIL it is in secret_words.
# Count and print the number of guesses made.
# A correct first guess should count as 1.

print()
print("Task 29:")
print()

secret_words = ["dragon", "robot", "python", "galaxy"]
word = input("Input a word: ")
guess = 1
while word not in secret_words: 
    word = input("Input a word: ")
    guess += 1 
print(guess)

# TASK 30:
# Create guests = [].
# Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# If a name is already in guests, reject it and ask again.
# Use a while loop, 'in' or 'not in', and append().
# Print the finished list and its length.

print()
print("Task 30:")
print()

guests = []
while len(guests) < 5:
    guest_name = input("Enter an unique guest name: ")
    if guest_name in guests: 
        guest_name = input("Enter an unique guest name please: ")
    else: 
        guests.append(guest_name)
print(guests)
print(len(guests))


# ============================================================
# SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# ============================================================

# TASK 31:
# Create a function named count_positive(numbers).
# RETURN how many elements are greater than 0.
# Do NOT use count().
# Test: count_positive([-2, 0, 4, 9, -1]) -> 2

print()
print("Task 31:")
print()

def count_positive(numbers): 
    count = 0 
    for i in numbers: 
        if i > 0: 
            count += 1
        else: 
            count = count 
    return count 

# TASK 32:
# Create a function named find_item(items, target).
# RETURN the index of the FIRST matching item, or -1 if missing.
# Do NOT use index().
# Test: find_item(["cat", "dog", "cat"], "cat") -> 0
# Test: find_item(["cat", "dog"], "fish") -> -1

print()
print("Task 32:")
print()

def find_item(items, target): 
    if target != items[0]: 
        return -1 
    else: 
        return items[0]

# TASK 33:
# Create a function named unique_items(items).
# RETURN a NEW list without duplicate values, preserving first
# appearance order. REQUIREMENT: Use 'not in'.
# Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]

print()
print("Task 33:")
print()


def unique_items(items): 
    new = []
    for i in items: 
        if i not in new: 
            new.append(i)
    return new

# TASK 34:
# Create a function named common_items(list1, list2).
# RETURN a NEW list of values found in BOTH lists.
# Include each matching value only once, in list1's order.
# REQUIREMENT: Use both 'in' and 'not in'.
# Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]

print()
print("Task 34:")
print()

def common_items(list1, list2): 
    add = []
    for i in list1: 
        if i in list2 and i not in add: 
            add.append(i)
    return add

# TASK 35:
# Create a function named reverse_list(items).
# RETURN a NEW list in reverse order, without changing items.
# Do NOT use reverse(), reversed(), or [::-1].
# Test: reverse_list([10, 20, 30]) -> [30, 20, 10]

print()
print("Task 35:")
print()


def reverse_list(items):
    new = []
    for i in items: 
        items[len(items)] = items[i] 

    return new 

# ============================================================
# SECTION 7 — DEBUGGING (TASKS 36–37)
# ============================================================

# TASK 36:
# Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# Explain in a comment what was wrong.
#
# number = 1
# while number <= 5:
#     print(number)
#
# Do NOT replace the while loop with a for loop.

print()
print("Task 36:")
print()

number = 1
while number <= 5:
    print(number)
    number += 1

# what was wrong is that, the system will be in a loop forever since the number never changed, and so it's always less than 5 

# TASK 37:
# Fix this code so it removes ALL 4s without skipping any.
# Explain in a comment why the original approach can fail.
#
# values = [4, 4, 7, 4, 9]
# for value in values:
#     if value == 4:
#         values.remove(value)
# print(values)
#
# Expected: [7, 9]
# HINT: A while loop and 'in' can help.

print() 
print("Task 37: ")
print()

values = [4, 4, 7, 4, 9]
while 4 in values: 
    values.remove(4)
print(values)

# the original approach can fail because when the first value that has four gets removed, all the numbers index get moved down by one number, and so the system can miss it because it already checked that value. 

# ============================================================
# FINAL BOSS CHALLENGES (TASKS 38–40)
# ============================================================

# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:
# 1. Add item
# 2. Remove item
# 3. View numbered items
# 4. Search for item
# 5. Exit
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.

print() 
print("Task 38: ")
print()

shopping_list = []

while True: 
    print("1. Add item")
    print("2. Remove item")
    print("3. View numbered items")
    print("4. Search for item")
    print("5. Exit")

    choice = input("Choose 1, 2, 3, 4, 5: ")

    if choice == "1": 
        item = input("Enter item to add: ")
        if item in shopping_list: 
            print("Item already exists")
        else: 
            shopping_list.append(item)
            print(item, "added")

    elif choice == "2": 
        item = input("Enter item to add: ")
        if item not in shopping_list: 
            print("Item not avaliable to be removed")
        else: 
            shopping_list.remove(item)
            print(item, "removed")

    elif choice == "3": 
        if shopping_list == []:
            print("Shopping list is empty")
        else: 
            print("Your shopping list: ")
            for number, item in enumerate(shopping_list, start = 1): 
                print(number, ".", item)

    elif choice == "4": 
        item = input("Enter itme to search for: ")
        if item in shopping_list: 
            print(item, "is in your shopping list")
        else: 
            print(item, "isn't in your shopping list")

    elif choice == "5": 
        print("Goodbye")
        break

    else: 
        print("Invalid, choose a valid number. ")


# TASK 39 — GRADE ANALYZER:
# Create a function named analyze_grades(grades).
# RETURN a list containing, IN THIS ORDER:
# [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# Passing means 70 or higher.
# Do NOT use sum(), min(), max(), or sorting.
# For an empty list, RETURN [].
# Test: analyze_grades([95, 82, 67, 74, 58])
# Expected: [95, 58, 75.2, 3, 2]
# Test with a single grade and all-negative values too.


def analyze_grades(grades):
    report = []
    highest_grade = 0 
    lowest_grade = 0 
    total = 0 
    average = 0 
    passing = 0 
    failing = 0  

    for i in grades: 
        if i > grades[0]:
            highest_grade = i 
    report.append(highest_grade)
    for i in grades: 
        if i < grades[0]:
            lowest_grade = i
    report.append(lowest_grade)

    for i in grades: 
        total += i 
        average = total/len(grades)
    report.append(average)

    for i in grades: 
        if i >= 70: 
            passing += 1
        else:
            failing += 1
    report.append(passing)
    report.append(failing)

    return(report)

analyze_grades([95, 82, 67, 74, 58])

# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# present = []
# absent = []
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
#   the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.

print() 
print("Task 40: ")
print() 

students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]

def attendance_percentage(present, students): 
    if len(students) == 0: 
        return 0 

    percentage = len(present)/len(students) * 100 
    return percentage 

        
def record(students): 

    present = []
    absent = []

    for i in students: 
        attend = input(f"Is {i} absent (A) or present (P)? ").strip()

        while attend != "P" and attend != "A": 
            print("Invalid")
            attend = input(f"Is {i} absent (A) or present (P)? ").strip()

        if attend == "P": 
            if i not in present and i not in absent:
                present.append(i)
        else: 
            if i not in absent and i not in present:
                    absent.append(i)
    print() 
    print("Present Students")
    for number, student in enumerate(present, start = 1): 
        print(number, ".", student)

    print() 
    print("Absent Students")

    for number, student in enumerate(absent, start = 1): 
            print(number, ".", student)    

    print("Number present:", len(present))
    print("Number absent:", len(absent))
    print("Attendance percentage:", attendance_percentage(present, students), "%")

    if len(students) > 0 and len(present) == len(students): 
        print("Perfect Attendance!")

record(students)

# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================
