#MODULE2 - DATA TYPES AND OPERATORES

x = 15
y = 20 

#Output operators test +
print('x + y =', x+y)

#Output operator test  - * / // **
print('x - y =', y-x)
print('x * Y =', x*y) 
print('x / y =', x/y)
print('x // y =',x//y)
print('x ** y =',x**y)



# Ok! I should pay attention to the content of cientific notation : m × 10 n
## (M vezes dez vezes elevado a potencia  de n), onde o expoente n é um numero inteiro 
# e o coeficiente m é qualquer numero real.
# 3,5 × 10² = 350 
# Most popular programming languages, 6.022E23(ou 6.022e23) 
# é equivalente a6.022 × 10²³ , e1.6 × 10 −³ seriam escritos1.6E-35

# Any real number can be writen like : m x 10N in many ways 
# # The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall *.9

rainfall *= .9
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5 
# print the new value of the reservoir_volume variable
print(reservoir_volume)

# Float is a real number to allow number with fractional values
# Int and Float are 2 types of data types 
# In python every object will have a type - O tipo de objeto definira quais operadores e funções funcionarão naquele objeto e como funcionarão.
#
#BOOLEANS
#Try comparison operators in this quiz! This code calculates the population densities of Rio de Janeiro and San Francisco.
#Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? Print True if it is and False if not.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

print(san_francisco_pop_density)
print(rio_de_janeiro_pop_density)

x=(san_francisco_pop_density > rio_de_janeiro_pop_density)
print(x)

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)
    
    #STRING - Practice

print("hello word") #double quotes
print('hello word') #single quotes 

welcome_message = 'hello my little friend! Are you still dead?'
print(welcome_message)

#pratice of using quotes
salesman = '" I think you\'re an enciclopedir salesman"'
print(salesman)

first_word, second_word = "hello", "space"
print(first_word + ' ' +  second_word) #If i put ' ' or " " between python will concatenate with space

word=("cobain")
print(word * 5) # How put spaces between ?

jhonatas_length = len("jhonatas")
benjamin_length = len("Benjamin")
print(jhonatas_length)

print(len("jhonatas") / len("benjamin"))
print(len("jhonatas") * len("benjamin"))
print(len("benjamin") + len("jhonatas"))
print(len("ben") + len("jhon"))


ford_quote = "Whether you think you can, or you think you can't--you're right." #With " " for define the value and ' ' for use on words
print(ford_quote)
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'#With ' ' for define the value and \ to add between the quotes of words.
print(ford_quote)

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

#The correct answer is 3415, and tropical_fruit_count is a string. That’s because even though the characters inside the string
#coconot_count and mango_count are number, but the values of variable tropical fruit count its a STRING with a + sign operator
#WAS TRICKY !


#You’ll be provided with example data for a user, the time of their visit and the site they accessed.
# You should use the variables provided and the techniques you’ve learned to print a log message 
# like this one (with the username, url, and timestamp replaced with values from the appropriate variables):

#Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

username = "Yogesh"
timestamp = "16:20"
url = "http://petshop.com/pets/reptiles/pythons"
print(username + ' ' + "acessed the site"+ ' ' + url + ' ' + "at" + ' ' +timestamp) #I dont know if i need put spaces like this?
print(username + " acessed the site " + url + " at " + timestamp) #If i dont put spaces between the quotes  and the sentence like "acessed the site" the output gonna give me like Yogeshacesses
#Remember in strings spaces matters for Python

#RIGHT ANSWER BY UDACITY
message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)

print (username + " accessed the site " + url + " at " + timestamp + ".")
#Use string concatenation and the len() function to find the length of a certain movie star's actual full name. 
#Store that length in the name_length variable. 
# on't forget that there are spaces in between the different parts of a name!

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# name_length = #todo: calculate how long this name is
name_length =(len(given_name + ' ' + middle_names + ' ' + family_name)) #Dont forget the spaces are importante. For python it matters
print(name_length)

name_length =(len(given_name + middle_names + family_name)+2) #Plus the spaces
print(name_length)

#OTHER SOLUTION
name_length = len(given_name) + len(middle_names) + len(family_name) + 2
print(name_length)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

# len(835) #Nice! The error message generated reads: TypeError: object of type 'int' has no len(), 
#which alludes to the fact that len only works on a "sequence (such as a string, bytes, tuple, list, or range)
#  or a collection (such as a dictionary, set, or frozen set)," as per the Python documentation.

#DIFERENTE TYPES OF VALUES - BUIT IN FUNCTION - TYPE
print(type(633))
print(type("633"))
print(type(633.0))

#Change the values for built what we want 
#1st example - We create a int from a float and assign it to a variable count  

count = int(4.0)
print(count)   
print(type(count))

#2nd example : We create a string as a House_number with the the value int for a house_number in the first moment.
#Bur using STR on the print function before putting (house_number) as her value will make possible create a phrase with the complete adress of the street.

house_number = 30
street_name = "Rua Candido de Sousa"
town_name = "braga"
print(type(house_number))
print(type(street_name))

adress = (street_name +" " +  str(house_number)+ " " + town_name)
print(adress)

#3rd Example : Built a number from a string 

grams = "35.0"
print(type(grams))
grams = float(grams)
print(type(grams))


mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
# IF I JUST WANT THE RESULT 
mon_sales = int(mon_sales)
tues_sales = int(tues_sales)
wed_sales = int(wed_sales)
thurs_sales = int(thurs_sales)
fri_sales = int(fri_sales)
print (mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales)
#IF I WANT THE STATEMENT
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convert the type back!!
print("This week's total sales: " + weekly_sales)

##METHOD
print("Jhonatas Gonçalo".title())
#Islower - If didn't exist any uppercase letters
full_name = "jhonatas gonçalo"
print(full_name.title())
print(full_name.islower())

print("One cat, two cat, withe cat, brown cat.".count('cat'))

print("Mohammed has {} balloons".format(27))

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

jhon_string = "Jhon loves {} and {}"
print(jhon_string.format("math", "statistics"))

#object = 13.37
#print(object.islower()) #AN ERROR OCCURS BECAUSE FLOAT HAS NO ATRIBUTE

string_doc_method = url
url = "https://docs.python.org/3/library/stdtypes.html#str.find"
print(url)

#split
new_str = "Benjamin is the most important thing in my life."
new_str.split() #Example how to use
print(new_str.split())

new_str.split(' ', 5) #Reference for print
print(new_str.split(' ',5))
#OR
new_str.split(None, 5)
print(new_str.split(None, 5))
#Using a periodo as separator
new_str.split('.')
print(new_str.split("."))

#\n causes a line break 

#PRACTICE
author = "Rudyard Kipling"
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse + ' ' + author)

print(len(verse))
print(verse.index('and'))
print(verse.index('you'))
print(verse.count('you'))

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))
#Other way

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))



#########################################################################
#MODULE 3 - DATA STRUCTURES

