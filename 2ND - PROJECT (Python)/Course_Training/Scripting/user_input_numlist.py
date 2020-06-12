# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


'''Solution for Quiz: Practice Debugging.
The code prompts the user for 10 two-digit numbers. 
It is supposed to then find and print the sum of all of the even numbers among those that were entered. 
But there is a bug in the code, because when I input a number, I get a TypeError.

How can I find the bug in the code and debug it?

I added a print statement to check the datatype of the variable holding the number input by the user. 
print(type(userInput)). I added this statement after the line userinput = input("Enter any number: ").
The output showed:
'class 'str' followed by TypeError: not all arguments converted during string formatting.
This meant that the variable userInput had a datatype of a string, but we need the datatype to be int instead.
The datatype for userInput needed to be changed to int.
To fix the error, I used the built-in function int()to return an integer object from the value input by the user.
See my solution below:'''

user_list = []  
list_sum = 0
for i in range(10):
    userInput = int(input("Enter any number: "))
    try:
        user_list.append(userInput)
        if userInput % 2 == 0:
            list_sum += userInput
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)

