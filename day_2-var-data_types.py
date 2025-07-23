#data types  and variables
a=5
b=True
c=1.1
d= complex(8,2)
e=2
f="hey crystal"
print(a+e)
print(f)
print("the data type of a is",type(a))
print("the data type of b is",type(b))
print("the data type of c is",type(c))
print("the data type of d is",type(d))
print("the data type of f is",type(f))

print("________________________________________")

# now there are list 
'''creation of list '''
my_list = [1, 2, "hello", 3.14]
empty_list = []
list_with_one_item = [5]


'''operations on a list '''

# Create a list
my_list = [10, 20, 30]
print("Original list:", my_list)
# 1. Change a value

my_list[1] = 99
print("After changing index 1:", my_list)

# 2. Add elements
'''appending methods only take one argument at once '''
# appending and extend both inserts element at last positions  
my_list.append(40)
print("After appending 40:", my_list)

my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

my_list.extend([50, 60])
print("After extending with [50, 60]:", my_list)
# extend can take multiple argument at once 


# 3. Remove elements
my_list.remove(99)
print("After removing 99:", my_list)
#  by using delete method we can delete any element at that position or index
del my_list[0]
print("After deleting element at index 0:", my_list)

# popping deletes the last element 
last_item = my_list.pop()
print("After popping last element:", my_list)
print("Popped item:", last_item)


# 4. Swap elements
my_list[0], my_list[1] = my_list[1], my_list[0]
print("After swapping index 0 and 1:", my_list)


# 5. Reverse and sort
my_list.reverse()
print("After reversing:", my_list)
my_list.sort()
print("After sorting:", my_list)
print ("popping ")

# 6. Replace a chunk using slicing
my_list[0:2] = [100, 200]
print("After slice replacement:", my_list)



''' tuples'''
#  there are also tuple
my_tuple = (1, 2, "hello", 3.14)
empty_tuple = ()
tuple_with_one_item = (5,)  # Note the trailing comma!

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
#This code creates two tuples of country names, combines them, and prints the result as a third tuple. Let me know if you'd like this turned into a list, sorted, or filtered!
''' note  
[] signifies a list (changeable).
() signifies a tuple (unchangeable), and remember the trailing comma for single-item tuples!'''

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)#used to count how many times a speciofic thing is appearing in that place or tuple
# res = tuple1.index(3) used to find the index or positon of a specific thing in a tuple or anywhere
res = tuple1.index(3, 4, 8)#here the first number is what we have to find and the other two numbers are the boundries of index that we have to find it from which position to which 
print('Count of 3 in tuple1 is:', res)


# now there are dictionaries 
my_dict = {
    'name': 'Alice',
    'age': 30,
}
print(my_dict)  

# format to change del or addd something in the dictionaries 

# Modifying
my_dict['age'] = 22

# Adding
my_dict['city'] = 'mumbai'

# Deleting
del my_dict['name']
print ("modified dictionary")
print(my_dict)
