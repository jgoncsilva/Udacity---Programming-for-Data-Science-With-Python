how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Jhon
"""


print(snake_string * how_many_snakes)

name = input('Enter a name:')
print('Hi', name.title())

#Since the input function interprets input as a String i need to wrap the result with "int" or "float" if a want to use as a number
#IF i Try a number like this

#num = input('Enter a number:')
#num += 20
#print(num)

#I will get an error but if i want use a number for this one it's just change the type


num = int(input('Enter a number:'))
num += 20
print(num)

#OR

num = float(input('Enter a number:'))
num += 20
print(num)

#IF i want to put a float and get the integer iterable for get, like if i'm multiplying a string to repeat it a certain number of times 

num = int(float(input('Enter a number:')))
print('hello' * num)

#EVAL - Other way to interpret user input. It's a built-in function that evaluates a string as a line of python. 

num = 30 
x = eval('num + 50')
print(x)

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

#TRY
try:
    x = int(input('Enter a number:'))
except : 
    print('That\'s not a valid number!')

print('\nAttempted Input\n')

#We could use a while loop on this case for  pause the loop (BREAK) to execute the code in the try block successfully executed

while True: 
    try:
        x = int(input('Enter a number:'))
        break
    except:
        print('That\'s not a valid number!')
    print('\nAttempted Input\n')

#If i put a right value this instruction on try block doesn't raise an exception 
#So moves on to the next line and BREAKS from the loop
#Since the breaks the loop never will print attempted input
#If i want to add "Attempted Input" Always theres an optional component of the statement we can use 

#FINALLY - Now "Attempted input " will be printed when the program is exiting this try statement

while True: 
    try:
        x = int(input('Enter a number:'))
        break
    except:
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')
        

#Useful to cleaning actions on the code 
while True: 
    try:
        x = int(input('Enter a number:'))
        break
    except ValueError:
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')
        

# The code on the finally block stil executed but! We can specify what error we can handle! On this case value error
# But Keyboard Error will close the program if i put for example Ctrl + C (because this is an KeyBoardValurError)

while True: 
    try:
        x = int(input('Enter a number:'))
        break
    except ValueError:#, KeyboardInterrupt could be putted here as a tuple with more the one type of exception
        print('That\'s not a valid number!')
    except KeyboardInterrupt: #Here two handlers for diferent blocks of code depending on the exception 
        print('\nNot attempted\n')
        break                #AFter check and no while loop 
    finally:
        print('\nAttempted Input\n') #Will print this and the KeyBoard error + no while loop
        

### EXERCICE

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people # TODO: Add a try-except block here to 
        leftovers = cookies % people 
    except ZeroDivisionError: #       make sure no ZeroDivisionError occurs.
        print("Ops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")
        
        
#When you handle an exception, you can still access its error message like this:


#ACESSING ERROR MESSAGES
cookies = 2
people = 1

try:
    num_each = cookies // people # some code just for fill 
except ZeroDivisionError as e:
    leftovers = cookies % people# some code " ''''' "
    print("ZeroDivisionError occurred: {}".format(e))

#IF I DONT HAVE ANY SPECIFIC EXCEPTION
# **********************except Exception as e:****************

#Exception is just the base class for all built-in exceptions.

#####################READING AND WRITING FILES ###############

#We can open with a built-in function called OPEN 
#Inclue OPEN (' STRING with the path to the file, along with optional parameters we want to especify')
f = open('/my_path/my_file.txt', 'r') 
f = open('notes.txt','r')
file_data = f.read()
f.close()

#It's importante to close because if we open and don't closing. We can run out the file handles and won't be able 
#to open any files create/we use like this

f = open('another_file.txt', 'w')
f.write('Hello Word')
f.close()

# WITH KEYWORD - Allow us to open the file ! Do operations on it ! And automatic closed after the idented code be executed
with open('another_file.txt', 'r') as f:
    file_data = f.read()
    ''' Description of how i used the with keyword
    The AS f: assigns the file object created by the open function to te variable name F
    This line of code f = open('another_file.txt', 'r') is almost the same i used above but with the new Keyword 
    The exception is that i can use only acess the file of the object with this block
    When you go out of the idented block the file is closed and we no longer able to interact with him 
    You can close the file but don't lose the data  '''
	
#Now i don't need 'F.CLOSE()'
# Calling file data outside the block works fine we can use of this file data methods on this file data string to 
#process contents
#Call the data file outside the block also works

#The READ METHOD 
#f you pass the read method an integer argument, it will read up to that number of characters, 
# output all of them, and keep the 'window' at that position ready to read on

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
    
    #READLINES() É um metodo para elr linha por linha
#In this case below! Python will loop over the lines of a file using the sintax for line in file.
#Because each line still has its newline character attached, I remove this using .strip().
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

#You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:  #use with to open the file filename - With open as f
        for line in f:      #use the for loop syntax to process each line - defining loop using f as a variable
            name = line.split(",")[0]  #and add the actor name to cast_list - split for lines in name
            cast_list.append(name) #Append cast_list for append the content of file : 'flying_circus_cast.txt'
    
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
    
    
'''The code prompts the user for 10 two-digit numbers.
It is supposed to then find and print the sum of all of the even numbers among those that were entered. 
But there is a bug in the code, because when I input a number, I get a TypeError.'''

#How can I find the bug in the code and debug it?

'''I added a print statement to check the datatype of the variable holding the number input by the user. print(type(userInput)).
 I added this statement after the line userinput = input("Enter any number: ").
The output showed:
'class 'str' followed by TypeError: not all arguments converted during string formatting.
This meant that the variable userInput had a datatype of a string, but we need the datatype to be int instead. 
The datatype for userInput needed to be changed to int.
To fix the error,'''
# I used the built-in function int()to return an integer object from the value input by the user. 

    
user_list = []  
list_sum = 0
for i in range(10):
    userInput = int(input("Enter any number: "))
    try:
        user_list.append(userInput)
        if userInput % 2 == 0: # check to see if number is even and if yes, add to list_sum
            list_sum += userInput
    except ValueError:# print incorrect value warning  when ValueError exception occurs
        print("Incorrect value. That's not an int!") 

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


#IMPORT SCRIPTS

#import - Special comand for import codes from other files, organize and reuse them.
#Should be used like this - import other_script (Import + name of the file without the .py)

#Eache one on separate line
#TOP of the code = is less confusing 
#Good pratice for readers for see what a script depends on

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


# useful_functions.py

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
    

#Using Python Standart library


# Use an import statement at the top

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():# Add your function generate_password here
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list) #It should return a string consisting of three random words 

# concatenated together without spaces

#OTHER OPITION 
#def generate_password():
    #return ''.join(random.sample(word_list,3))


# test your function
print(generate_password())


#IMPORT 

import math #import modules (.notation is necessary)
from math import pow #import an object from module #Use the name without .notation - no needed
import os.path #import submodule (Remember to use )
os.path.isdir('My Path') #import a submodule and using one object from .notation is necessary
#I cannot import a module like this :
'''import os.path.isdir ''' #THIS WILL RESULT AN ERROR 
'''from math import * - Actually it's not ok use * for import all of the objects, it's better just import the entire module and use .notation for specify the objects i'll use'''
from datetime import datetime #Import class datetime and the module datetime if i refer to 'datetime' i'll refer to CLASS and not to module
#Modules that are submodules are specified by the package name and then the submodule name separated by a dot.
# I can  import the submodule like this.
import package_name.submodule_name

#PIP
#standart package manager for install libraries 
#FOR INSTALL ALL OF THE DEPENDENCIES OF A PROJECT  : pip install -r requeriments.txt
#ANACONDA is designed for Data science

#for instal - on the command line use pip install pytz for example 
#1) Recommend import first the standart libraries before import third-party packages 
#like this 

from datetime import datetime
import pytz

#Requirements.txt - list of project dependencies 
#name of the package and version (optional but should be included)


''' IPython - A better interactive Python interpreter
requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
Flask - a lightweight framework for making web applications and APIs.
Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
pytest - extends Python's builtin assertions and unittest module.
PyYAML - For reading and writing YAML files.
NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
ggplot - Another 2D plotting library, based on R's ggplot2 library.
Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
pyglet - A cross-platform application framework intended for game development.
Pygame - A set of Python modules designed for writing games.
pytz - World Timezone Definitions for Python '''

'''How to Search
Here are some techniques for effective web searching:

Try using "Python" or the name of the library you're using as the first word of your query.
This tells the search engine to prioritize results that are explicitly related to the tools you're using.
Writing a good search query can take multiple attempts. If you don't find helpful results on your first attemp try again.
Try using keywords found on the pages you found in your initial search to direct the search engine to better resources in the subsequent search.
Copy and paste error messages to use as search terms. This will lead you to explanations of the error and potential causes. An error message might include references to specific line numbers of code that you wrote. Only include the part of the error message that comes before this in your search.
If you can't find an answer to your question, ask it yourself! Communities like StackOverflow have etiquette rules you must learn if you want to participate, but don't let this stop you from using these resources.'''

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower
#function that creates a flower_dictionary from filename
import flower txt 

def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()