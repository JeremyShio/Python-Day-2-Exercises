# ------- Week: 2 Day: 2 Homework -------




# ------- Exercise 1 -------
# Create a list of numbers that are less than ten using l_1 and list comprehension
# Use the following list - [1,11,14,5,8,9]
# Your output should [1,5,8,9]

l_1 = [1,11,14,5,8,9]

def less_than_ten(l_1):
    number_list = []
    for number in l_1:
        if number < 10:
            number_list.append(number)
    print(number_list)

print('')            
print(less_than_ten(l_1))




# ------- Exercise 2 -------
# Using list comprehension, create a list of names of 4 letters or more and capitalize each name
# Output: ['Connor', 'Connor', 'Connor', 'Evan', 'Evan', Kevin']

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

def valid_names(names1):
    new_names = []
    for name in names1:
        if (len(name) > 3):
            new_names.append(name.title())
    print(new_names)

print('')
print(valid_names(names1))




# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

def is_name(names2):
    new_names = []


print('')
print(is_name(names2))

