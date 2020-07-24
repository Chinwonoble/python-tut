#  a set is a collection which is unordered and unindexed. no duplicate members. 

# create set
fruits_set = ('apples', 'oranges', 'mango')

# check if in set
print {'apples', 'oranges', 'mango'}

# check if in set
print ('apples' in fruits_set)

# add to set
fruits_set.add ('grape')

# remove the set
fruits_set.remove('grape')

# add duplicate
fruits_set.add('apples')

# clear set
fruits_set.clear()

# delete
del fruits_set

prints(fruits_set)