##LOOPS
fruits=['apple','banana','orange']
for fruit in fruits:
    print(fruit)
    print(fruit + ' Pie')
print(fruits)
#sum
student_score=[10,14,15,9]
total_exam_score=sum(student_score)
print(total_exam_score)
sum=0
for score in student_score:
    sum+=score
print(sum)
#max
student_score=[10,14,15,9]
print(max(student_score))
max_score=0
for score in student_score:
    if score >max_score:
        max_score=score
print(max_score)
#sum 1_100
total=0
for number in range(1,101):
    total+=number
print(total)
#password gen
import string
import random

letters = list(string.ascii_lowercase)
numbers = list(range(1, 11))
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Password Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

password_list = []

# Add random letters
for i in range(nr_letters):
    password_list += [random.choice(letters)]

# Add random symbols
for i in range(nr_symbols):
    password_list += [random.choice(symbols)]

# Add random numbers
for i in range(nr_numbers):
    password_list += [random.choice(numbers)]

# Mix them randomly
random.shuffle(password_list)

# Convert list to string
password = ""
for char in password_list:
    password += str(char)

print(f'Your password is: {password}')
#functions
def my_function():
    print('hello')
    print('bye')
my_function()

cats=7

#while something_is_true:
while cats>0:
    print('cute cat')
    cats-=1
