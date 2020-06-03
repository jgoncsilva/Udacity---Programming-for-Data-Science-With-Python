#MODULE 3 - DATA STRUCTURES

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'Octorber', 'November', 'December']
print(months[0])
print(months[-1]) 

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])
print(list_of_random_things[3])
# print(list_of_random_things[len(list_of_random_things)]) #Erro because the list have multiple types of operators
print(list_of_random_things[len(list_of_random_things) - 1])
print(list_of_random_things[-2])
print(list_of_random_things[:2])
q3 = months[6:9]
print(q3)
print('Sunday' in months, 'Sunday' not in months)


my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
#['one', 2, 3, 4, 5]

#sentence1 = "I wish to register a complaint."
#sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]


#["I","wish","to","register","a","complaint","!" # SENTENCE [6] = "!"
#["Our majesty", "wish", "to","register", "a", "complaint"] #sentence2[0] = "Our Majesty"
#"I wish to register a complaint" #sentence1[30] = "!" #error
#["We", "want", "to", "register" "a", "complaint"] #sentence [0:2 = ["We, want"]]

#Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. 
#For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = 2
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]


# use list indexing to determine the number of days in month
num_days = days_in_month[month - 1]
print(num_days)

#Estrategy is because in python the count starts in 0 put the index variable to start by the last month - On this case -1 or December
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates)
print(eclipse_dates[-3:])

VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
print(VINIX[0])
print(VINIX[23])
print('GE' in VINIX)

name = 'Jim'
stundent = name
name = 'tim'

print(name)
print(stundent)

scores = ["B", "C", "A", "D", "B", "A"]
grades = scores

print("scores : " + str(scores))
print("grades: " + str(grades))

#About list : 1) Len returns how many elements are in the list, 2) Max - Returns the greatest element on the list.
#3) The max element of number depends o what type of objects - In a list of 
#a) Numbers : Is the max number
batch_sizes = [15, 9 ,12, 89, 96, 24, 35]
print(batch_sizes)
#The max function is defined by the greater than (>) comparison  operator
#b) Strings - Will be the element that occurs less - In alphabetic order like on the e.g bellow
python_varieties = ['Burmese Python', 'African Rock Python', 'ball python', 'reticulated python', 'angolan python']
print(max(python_varieties))
#About the case above R is the largest letter alphabetically, greater then B, A.
#The max function is defined by the last element that show alphabetically.
#The MAX Function doesn't work (is undefined) for list that contains elements from diferent incomparable types. 


##MIN - Opposite of max and returns the smallest element in a list
##SORTED - Returns a copy of a list ordered from smallest to largest leaving the original list unchanged
print(sorted(batch_sizes))
print(sorted(batch_sizes, reverse =True))

##JOIN  - String Method
#Separate String 
nautical_directions = "\n" .join(["fore", "aft", "starboard"])
print(nautical_directions)
namez = ["Garcia", "O'kelly", "Davis"]
print("-".join(namez))

#APPEND
python_varieties.append('Bloody Python')

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#4,2 Output - This is gonna happen because on this case len counts the number of arguments inserted on the variable. A) 3 b) 4 c)2

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

#Output - Albert & Ben & Carol & Donna - Sorted is gonna copy without change the list, but will display output alphabetically the strings join with " & " Between them.

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

#Output - ["Albert", "Ben", "Carol", "Donna", "Eugenia "] - Same reason of the 

##TUPLES 
Gotham = (13.4125, 103.86667)
print(type(Gotham))
print("Gotham wat is at latitude : {}".format(Gotham[0]))
print("Gotham wat is at longitude : {}".format(Gotham[1]))

#Compact Way  - 
dimensions = 52, 40, 100 #No parentheses, just use for clarify the code 
length, width, height = dimensions #Tuple Unpacking - Use information from a tuple into multiple variables without have to acess them one by one and make multiple assignmente statments
print('The dimensions are {}x{}x{}'.format(length, width, height)) 

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

##SETS
countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana'] #777 More countries were displayed

print(len(countries))
print(countries[:5])

country_set = set(countries)
print(country_set)
print('India' in countries)
print('India' in country_set)
country_set.add('Italy') #We don't use append like we use in lists
print('Italy' in country_set)

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

#List a has 10 elements, 
#while the set b (created from the list a) has 4 elements because the are 4 unique elements in a. 10 - 4 = 6.

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
# i don't know if 5 its gonna be part of the set because OF pop, the element 5 can be excluded

#DICTIONARY


dct ={'milk' : 5.0, 'bread' : 1.1, 'coffe' : 2.0, 'Ilo' : 1.2}
#dct[key] = value - Pattern for add new values to or dct.update({another dictionary})

print(dct)
elements = {'hydrogen': 1, 'helium':2, 'carbon': 3}


x = elements.get ('dilithium')
not_null = x is not None
print(not_null)
print("carbon" in elements)
print(elements.get("dilithium")) #get returns none 
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 6  # insert "lithium" with a value of 3 into the dictionary
n = elements.get("dilithium")
print(n is None)
print(n is not None)

population = {'Shangai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print('population :', population)

elements.get('kryptonite', 'There\'s no such element!') #Define the default value to be returned instead of None
"There's no such element!"

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

VINIX =  {'C': 0.74, 'MA': 0.78, 'BA': 0.79, 'PG': 0.85, 'CSCO': 0.88, 'VZ': 0.9, 'PFE': 0.92, 'HD': 0.97, 
          'INTC': 1.0, 'T': 1.01, 'V': 1.02, 'UNH': 1.02, 'WFC': 1.05, 'CVX': 1.05, 'BAC': 1.15, 
          'JNJ': 1.41, 'GOOGL': 1.46, 'GOOG': 1.47, 'BRK.B': 1.5, 'XOM': 1.52, 'JPM': 1.53, 'FB': 2.02,
          'AMZN': 2.96, 'MSFT': 3.28, 'AAPL': 3.94}
VINIX = {'C': [0.74, -6.51],  'MA': [0.78, 34.77],  'BA': [0.79, 17.01],  'PG': [0.85, -8.81],  'CSCO': [0.88, 18.56], 
          'VZ': [0.9, 2.16],  'PFE': [0.92, 13.96],  'HD': [0.97, 3.2],  'INTC': [1.0, 2.61],  'T': [1.01, -15.19], 
          'V': [1.02, 24.0],  'UNH': [1.02, 19.32],  'WFC': [1.05, -3.59],  'CVX': [1.05, -5.77],  'BAC': [1.15, 4.27], 
          'JNJ': [1.41, -5.58],  'GOOGL': [1.46, 17.84],  'GOOG': [1.47, 17.03],  'BRK.B': [1.5, 4.54],  'XOM': [1.52, -6.87],
          'JPM': [1.53, 7.66], 'FB': [2.02, 0.91], 'AMZN': [2.96, 62.75], 'MSFT': [3.28, 26.61], 'AAPL': [3.94, 26.01]}  
print(VINIX)

#  A dictionary is a mutable, unordered data structure that contains mappings of keys to values.
#Because these keys are used to index values, they must be unique and immutable. 
#For example, a string or tuple can be used as the key of a dictionary,
#but if you try to use a list as a key of a dictionary, you will get an error.

elemento = {'hidrogenio': {'number': 1,
                           'weight': 1.00974,
                           'symbol': 'H'}, 
            'helium': {'number': 2,
                       'weight': 4.002602,
                       'symbol': 'hl'}}
print(elemento['helium'])
print(elemento.get('unsainted', 'theres no match element!'))

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

#IsNoble
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split() #USE OF SPLIT for separate words
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list) #colelcting unique elements
print(verse_set, '\n')

# print the number of unique words
num_unique =  len(verse_set) #We use len  "Count" in SQL it's almost the same idea (I think) 
print(num_unique, '\n')

#How many unique words are in verse_dict?
#Is the key "breathe" in verse_dict?
#What is the first element in the list created when verse_dict is sorted by keys?
#Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. Use this list of keys to answer the next two questions as well.
#Which key (word) has the highest value in verse_dict?

### DICTIONARY
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 



#############################################################################