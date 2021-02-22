#Nested if else statements
#1. Write a funtion that takes in someone's age if their age is a multiple
#of 5 tell them they win a free vacation. If their age is also a multiple of 5
#tell them they win a car. If their age is also an even number tell them they win
#a house

def prize(age):
    if age % 5 == 0:
        if age % 10 == 0:
            if age % 2 == 0:
                print("You win a house")
            else:
                print("You win a car")
        else:
            print("You win a vacation")
    else:
        print("No prize")

age = int(input("Enter your age: "))
prize(age)

#2. write in a function that takes in a number and tells the user if the number
#is a positive single-digit number. If it is a positive single digit number, tell
#the user that it is a positive single digit number. Otherwise, tell the user it
#not a positive single digit number. 

def isPosSingleDig(num):
    if num > 0:
        if num < 10:
            print("Is a positive single digit number")
        else:
            print("Is not a positive single digit number")
    else:
        print("Is not a positive single digit number")

num = int(input("Enter a number: "))
isPosSingleDig(num)

#And Or
#Write a function that does the same thing as the functions described above
#but uses and or statements instead of nested if else statements

def prizeAO(age):
    if (age % 5 == 0) and (age % 10 == 0) and (age % 2 == 0):
        print("You win a house")
    elif (age % 5 == 0) and (age % 10 == 0):
        print("You win a car")
    elif (age % 5 == 0):
        print("You win a free vacation")
    else:
        print("No prize")

def isPosSingleDigAO(num):
    if num > 0 and num < 10:
        print("Is a positive and single digit number")
    else:
        print("Is not a positive and single digit number")

#for loops
#1. Write a function called count down which takes in an integer and counts down by
#3s until you get to zero. Print the index for each iteration of countdown and
#let the user know if that index is even or odd.

def countDown(num):
    for i in range (num, -1, -3):
        print(i)
        if (i % 2 == 0):
            print("The number is even")
        else:
            print("The number is odd")

num = int(input("Enter a number: "))
countDown(num)
    
#2. Write a function that takes in a string and uses a for loop to reverse that
#string.

def reverseString(s):
    reversedString = ""
    for c in s:
        reversedString = c + reversedString
    print(reversedString)

s = "dog"
reverseString(s)

#While loops
#1. Write the reverse string function using a while loop

def reverseString2(s):
    reversedString = ""
    length = len(s) - 1
    while length >= 0:
        reversedString = reversedString + s[length]
        length = length - 1
    print(reversedString)

s = "cat"
reverseString2(s)

#2. Write a function that takes in a secret number between 1 and 10. Ask the
#user to keep guessing the secret number until they guess correctly.

def guessMyNum(secretNum):
    num = int(input("Enter a number between 1 and 10: "))
    while (num != secretNum):
        num = int(input("Wrong number! Guess again: "))
    print("You guessed my number!")

guessMyNum(5)
