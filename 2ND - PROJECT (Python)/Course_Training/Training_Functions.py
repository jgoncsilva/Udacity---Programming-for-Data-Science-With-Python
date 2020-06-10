def cylinder_volume(height, radius):      #HEADER - DEF KEYWORD ALWAYS FIRST - NAME OF THE FUNCTION (cylinder... Without spaces) - ARGUMENTS ( ) - ENDS : - 
    pi = 3.14159
    volume =  height * pi * radius ** 2 
    return volume

# Return - Used for give back the output value when the function is called
# Remember some functions like print don't return anything at all. 
return_value = print('Hey wait i have new complaint, forever in debt to your priceless advice')
print('Output:', return_value)

#print provide output for the console 
#while return provide the value that i can store and work / code later.
#Is not necessary that every function have a return statement

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))  


#DEFAULT ARGUMENT 

def cylinder_volume(height, radius=5):  #if radius it's not specified then the variable radius will default=5 when used in the functon body 
    pi = 3.14159
    return height * pi * radius ** 2

#So if we call (print) like this :
print(cylinder_volume(10, 5))
#is the same if i call this : because radius is set five if not specified other value. 
print(cylinder_volume(10))

#Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values.
# I've included two test cases that you can use to verify that your function works correctly.
#Once you've written your function, use the Test Run button to test your code.
def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

#Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
#For example, calling the function and printing the result like this:

def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
#print(readable_timedelta(10))

###### VARIABLE SCOPE


#(OPEN)def word_count(document, search_term):
    #words = document.split()
    answer = 0 
    for word in words:
        if word == search_term:
            answer += 1
    return answer
#print(answer)
#The first function uses answer to count word in a document
#(OPEN)def nearest_square(limit):
    answer = 0
    while (answer + 1) ** 2 < limit:
        answer += 1
    return answer**2
#print(nearest_square(1))
#The second function uses answer to check value while searching for the nearest square

#Both functions include this answer variable, but they are distinct variable that can only
#be referenced with their respective functions

ans = 10

def show_ans():
    print(ans)

show_ans()
print(ans)

# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"

# This works fine
word = "hello"

def some_function():
    print(word)

some_function()

#THIS CODE BELLOW RESULTS IN A ERROR
#egg_count = 0

#def buy_eggs():
    #egg_count += 12 # purchase a dozen eggs

#buy_eggs()

#This causes an UnboundLocalError, since Python doesn't allow functions to modify variables that are outside the function's scope.
#  A better way would be to pass the variable as an argument and reassign it outside the function. 
#Like this 
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)

str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

#When we call the function we use str1 = 'Variable scope is an important concept.' wich has a local variable scope

str1 = 'Functions are important programming concepts.'

def print_fn():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

#When i put # before 'str1 Variable' i'm removing the local scope by transforming in a comment.
#the valid str1 above has a global scope, when i call the function will print because of the global scope.
#This code Bellow result in error because i'm trying to print the function with an argument, but the function doesn't have. 
#(open)def print_fn():
    #str1 = 'Variable scope is an important concept.'
    #print(str1)

#print_fn(str1)


##DOCSTRING
# """ (Triple quotes)
#FIrst line : breaf explanation of the functions purpose (Docstring in one line are perfect acceptable)
# Can add a paragraph after the resume in oneline  - EXPLANATION OF THE FUNCTION ARGUMENTS

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area


def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

#LAMBDA EXPRESSIONS 

#Used to create anonimous functions 
#Use for functions that accept other function as an argument

def double(x):
    return x * 2

double = lambda x: x * 2
#function / Lamba expression / one or more argumentos for the anonymous function and then a colon/ expression that is evaluated and returns this function 
double = lambda num: num * 3
#Can be useful for short and simples functions 
#If i want to specify multiple arguments in a lambda function can include then before the colon separated by commas
lambda x, y: x * y #multiple two numbers together

#Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

#First idea was start with numbers but 'numbers' it's a variable who i will use for reference
#I realized that : The objective is to find averages so i need the list(map for get the results
#So! i need define some function but remember that whats in inside is evaluated first
#(lambda x: sum(x)/ len(x), then use numbers


#Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)