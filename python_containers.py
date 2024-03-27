# Exercise 1
# Create a list named students containing some student names (strings).

students = ['Abby', 'Jessica', 'Albert', 'John']

# Print out the second student's name.

print(students[1])

# Print out the last student's name.
print(students[-1])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.

foods = ('sushi', 'burger', 'pizza', 'curry')

# Use a for loop to print out the string "[food goes here] is a good food".

for food in foods:
    print(f"{food} is a good food")


# Exercise 3
# Using a for loop, print just the last two food strings from foods.
for food in foods[-2:]:
    print(food)

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
    
home_town = {
    'city': 'Cary', 'state': 'NC', 'population': '2,000,000'
}

# Print a string with this format:
# "I was born in city, state - population of population"

print("I was born in {}, {} - population of {}".format(home_town["city"], home_town["state"], home_town["population"]))

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

for key, value in home_town.items():
    print(f"{key} = {value}")


# Exercise 6
# Create an empty list named cohort.

# Using a for loop to iterate over the students list.

# Hint: Use the enumerate function to provide both the index & student

# Within the for loop, add a dictionary to the cohort list that combines the student's name and the food in the foods list at the same index. Each dictionary will have this shape:

#  {
#    'student': 'Tina',
#    'fav_food': 'Cheeseburger'
#  }
# Iterate over the cohort list, printing out each item (it's not necessary to format the dictionaries).
    
cohort = []

for index, student in enumerate(students):
    student_food = {
        'student': student,
        'fav_food': foods[index]
    }
    cohort.append(student_food)

# Printing out the cohort list
for item in cohort:
    print(item)


#Excercise 7

awesome_students = [student + " is awesome!" for student in students]


for student in awesome_students:
    print(student)

## Exercise 8

for food in [food for food in foods if 'a' in food]:
    print(food)
