# a list is a collection which is ordered and changeable. allows duplicate members.

# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes','pears']

# use a constructor
# number2 = list ((1,2,3,4,5))

# get a value
print(len(fruits))

#append to list
fruits.append('mango')

# remove from list
fruits.remove('grapes')

# insert into position
fruits.insert(2, 'strawberries')

# change values
fruits[0] = 'blueberries'

# remove with pop
fruits.pop(2)

# reverse list
fruits.reverse()

# sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=true)

print (fruits)
