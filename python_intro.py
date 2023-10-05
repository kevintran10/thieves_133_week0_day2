#comments! This is a comment
print('hello thieves')   # we can write comments here too!    #this print statement greets the user
# safsd
#  fds           to comment in bulk us:  Ctrl + /
#  asdf



# To-Do
#
# Variables
x = 5


# Data Types!  Starting with numbers
# Integers and Floats
num1 = 8
print(num1)
print(type(num1))

num2 = 8.0
print(num2)
print(type(num2))

num3 = 5.898234
print(type(num3))

# Math operations!
print('Math!!!\n')

# Add +
add = 5 + 5
print(add)

# Subtraction -
sub = 10-5
print(sub)

# Multiplcation *
prod = 5*5
print(prod)
print(type(prod))

# Division  /      Whenever using division the result of this will always be a float
div = 25 / 5
print(div)
print(type(div))

# Exponents **
powerful = 5 ** 2
print(powerful)

# Floor division //         How many times does 5 go into 26, Goes into 26 five(5) times with a remainder/modulo % of 1
fdiv = 26 // 5
print(fdiv)

# module %          # Remainer  # This will become very handy VERY soon anytime we want to determine odd or even
mod = 26 % 5
print(mod)        
    # This will become very handy VERY soon anytime we want to determine odd or even
print(25 % 2 == 0)    # Meaning that the result should be even, but this is False because 2 doesn't go into 25 evenly.
print(24 % 2 == 0)    # True statement, written differently
print(25 % 2 != 0)    # True statement, written differently

# Lets talk about equal signs/equality
#  =   this is assignment
#  ==  this is an equility check /// checking for type AND value equality
#  != not equal to

print('5' == 5)      # this is a false statement

# Strings
print('\nSTRINGS\t:')    #    \n = new line  ;   \t = tab
# they're ordered, immuteable, iterable
# you can use single '' or double "" quotes, either is fine BUT watch the interaction

st1 = 'single quote string'
st2 = "double quote string"
st3 = "we've messed this up"      # <--- invalid syntax error
st4 = 'or did we "really?"'
st5 = 'oh no we\'ve messed this up'    # <--- escape character, \ ignore this next character
print(st5)

# Ordered
print(st1[-3])
print(len(st3))
# Iterable - means we can go through them/strings, step by step

# Maninuplating strings

# Concatenation(adding together pieces of string) + Interpolation (f-string and maybe don't to remember this term exactly)

# Concatenation
print(st1 +st4)    # simple
print(st2 + ' : ' + st3)   # adding a literal
print(st2 + ' ' + str(mod) + ' ' '<--that was little funky' )  #complicated example

# f-strings (or interpolation if you're fancy)

f_st = f"this is still just a string BUT we can include phythony things like {mod} or {st1[-6]}"
print(f_st)

# String methods
print(st5.upper())
print(st5)


# Incrementing and decrementing a variable
num5 = 234
num6 = 98734
print(num5 + num6)
print(num5, num6)

num5 = num5 + 6    # this is the long-hand version
print(num5)

num5 += 10      # this is the short-hand version
print(num5)

num5 -= 100     # can be used with other math operators as well
print(num5) 

num5 *= 100
print(num5)

f_st += ' I"M ADDING THIS!!!'
print(f_st)





# Functions / "function()" vs Methods / ".method()"
# syntax --> function(arguments) vs dataype.method(aruguments)


# Lists
# Indexed, ordered, iterable, muteable, dyanmic
# syntax --> defined with brackets []   example(s):    alist = [1, 2, 3, 4]  //  alist = []  
a_list = []
print(a_list)
nums_list = [10, 20, 30, 40, 50]
print(nums_list, type(nums_list), len(nums_list), nums_list[0], nums_list[-1])
nums_list[0] = 60986095

print(nums_list)
rando_list = [1, '2', 3.0, True, None, []]
print(rando_list)
print(rando_list[3])

print('list methods:')
# .append()
# adds to the END of the list
print(a_list.append(5))
print(a_list)
a_list.append(15)
print(a_list)
a_list.append(25)
print(a_list)

# .pop
# removes an item from teh list by position, defaults to the LAST! AND!!! returns the value so you could save it to a variable...
a_list.pop()
print(a_list)
print(a_list.pop(0))
print(a_list)

# .remove()
# remove or takes out the FIRST occurence of a VALUE     think of it as reading LEFT to RIGHT, whenever it sees the first VALUE looking for, it's going to remove that and not the other identical values
a_list.append(50)
a_list.append(75)
a_list.append(50)
print(a_list)
a_list.remove(50)
print(a_list)

# sort and sorted
print('\n\nsorted:')
print(sorted(a_list))
print(a_list)
print('\n.sort')
a_list.sort()
print(a_list)



print('\n\nString example with slicing:')
# f_st[0] = 'Z'   -->  
# slicing -->  [start :stop: step]  first example --> [:] aka --> [start:end]
x = 'Z' + f_st[1:]
print(x)


print('\nLOOPS')
# 3 types of Loops:   for loop, index loop, and while loop
names = ['Lee', 'Stephen', 'Jeni', 'Gianni', 'Heather', 'Kevin']

print('for loops:')
# for loop --> syntax:
# for item in items:
#   codeblock to run on item
step = 1
for name in names:
    print(name.upper())


for a in a_list:
    print(a**8)

# index loop . . . but first, did we talk the range function?
# let's talk about the range function:
for x in range(5):
    print(x)
print('\n')
for x in range(0, 5, 1):
    print(x) 
print('\n')    
for x in range(50, 10, -10):
    print(x)
for x in range(3):
    print('3 steps taken')

# back to the index loop:
# syntax --> 
#   for i in range(len(iterable)):
#       codeblock
print('\nINDEX loop')
for i in range(len(names)):
    print(i, names[i])

# while loops
# syntax -->
# while condition:
#   codeblock
while True:
    print('bad idea')
    break

l = 0     # l as in left
while l < len(names):
    print(l, names[l])  
    l += 1


# Conditionals:    if, elif, else
# syntax -->   if condition:
#                 code to execute
if 3 < 1:             # creates a False statement, so the 'duh' will not show up in the terminal.
    print('duh')
if names[0] == 'Lee':
    print('it is Lee!')
elif names[0] == 'Jeni':
    print('it is Jeni')
elif names[0] == 'Eddie':
    print('Eddie is in the list!')
else:
    print('We don\'t know this person')


age = 2

if age < 18:
    print('You are a kid')
elif age > 64:
    print('You are a senior')
else:
    print('You are a adult')

# Functions
# defintion vs calling the function
def hello(name):     # (name) is a parameter aka ingredients to making a recipe
    print(f"OMGosh So happy you are here {name.upper()}!")
    

hello('Jeni')          # equivalent to you making the recipe
hello('Kevin')
print(hello(st3))

# Difference between print vs return
# print is asking what is the VALUE of the line is

def adder(a, b):
    return a + b
def subtr(a, b):
    print(a-b)

adder(6, 5)
subtr(10, 5)
subtr(adder(6, 5), 6)
# adder(subtr(67, 5), 98)    # this line causes an error because (subtr(67, 5)) returns NONE


# user = input('this is what shows on the screen and asks you to type something --->     ')
# print(user)

# if 'a' in user:
#     print('Yep it is')

print(names)
names.remove('Jeni')
if 'Jeni' in names:
    print('Yep')
else:
    print('Not found')






# 'protected' words/terms --> be careful with our variable names!!!
# int = 234234      <-- Don't redefine protected words!!!
# print(int('5'))




