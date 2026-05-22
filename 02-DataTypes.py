print('Hello'[0]) #this is subscripting . Result H
print('Hello'[4])
print('Hello'[-1])

print('Hello'[0:3]) #this is slicing . Result Hel

# len(1234) #gives an error since its not a string
len('1234') #gives 4 since its a string

print(type('Hello'))
print(type(1234))
print(type(3.14))
print(type(True))
print(type(None))

print(int('123') + int('456')) #result 579
print(float('3.14') + float('2.71')) #result 5.85
print(str(123) + str(456)) #result 123456
print(bool(0)) #result False
print(bool(1)) #result True
print(bool('')) #result False
print(bool('Hello')) #result True

print("Number of letters in your name: " +str(len(input("Enter your name: "))))#str will turn the input msg from int to string then we can concatinate

print(4+2)
print(4-2)
print(4*2)
print(4/2)
print(4//2) #floor division it takes the reminder away and givees only the int number
print(4%2) #modulo operator gives the remainder
print(4**2) #exponentiation operator

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) #this flours the number
print(round(bmi)) #this rounds the number to the nearest whole number
print(round(bmi, 2)) #this rounds the number to 2 decimal places

score =0
score += 1 #this is the same as score = score + 1
print(score)
score -= 1 #this is the same as score = score - 1
print(score)

score = 0
height=1.8
is_winning=True
print(f"Your score is = {score}, your height is = {height}, you are winning is {is_winning}") #f string is like `` in js it allows us to use {} to insert variables into the string

#Project: Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10,12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")

