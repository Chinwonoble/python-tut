# strings in python are surronded by either single or double quotation mars. Lets look at string formatting and some string methods
name = 'noble'
age = 16

# concatenate 
print ('hello , my name is' + name + 'and I am' + str(age)+ 'that is actually my age')

# String formatting

# arguements by position
print ('My name is {name} and I am {age}'. format ( name=name, age = age))

# f- string (3.6+)
print (f' Hello, my name is {name} and I am {age}')

# string methods

s = 'helloworld'

# capitalize string
print (s.capitalize())

# make all uppercase 
print (s.upper())

# make all lower
print (s. lower())

# swap case
print (s.swapcase())

# get length
print (len(s))

# replace
print (s.replace('world', 'everyone'))

# count
sub = 'h'
print (s.count(sub))

# starts with
print (s.startswith('hello'))

# ends with
print (s.endswith('d'))

# split into a list 
print (s.split())

# find position
print (s.find('r'))

# Is all alphanumeric
print (s.isalnum())

# is all alphabetic
print (s.isalpha())

# is all numeric
print (s.isnumeric())





