'''
Filename: random_student.py
Purpose: randomly select student
'''
# Modules
import random # adding a module/library (not a package that's ES6 land)

# Variables
student_list = ["Brice", "Jake", "Taylor", "Jacks", "M", "Sandra", "Paul", "Gabe", "Ryan", "Nick"] # populating a list object

# two empty lists
present_students = [] # creates a list object w 0 members
absent_students = [] # "

# range() must just work like a forEach()...
# len() def returns an integer that's the count of list items
for x in range(len(student_list)): # sets up a loop that will repeat for each list item, no matter how long the list!
    selected_student = random.choice(student_list) # random has methods? so choice() function, from random module

    print(f"Chosen student: {selected_student}") # inserts the list item chosen above

    present = input(f"Is {selected_student} here? ") # stores feedback from user, seems to be asking for a yes/no but it's not specific

    # boolean aka either/or block, works for a literal 'yes' reply but nothing else-- trying to create multiple options
    if present == ("yes" or "y"):
        present_students.append(selected_student) # append = adds to list
    else:
        absent_students.append(selected_student)

# oh snap, does this return a list of attendees, based on yes answers?? nice
    student_list.remove(selected_student)

print("\nPresent Students: ✅")

for student in present_students:
    print(student)

print("\nAbsent Students: 🎒")

for student in absent_students:
    print(student)
