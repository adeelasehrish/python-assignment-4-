#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Python program for simple calculator

# Function to add two numbers
def add(x,y):
     return x + y

# Function to subtract two numbers
def subtract(x,y):
     return x - y

# Function to multiply two numbers
def multiply(x,y):
    return  x * y

# Function to divide two numbers
def divide(x,y):
    return x / y

# function gives power
def power(x,y):
    return x^y

print("Please select operation -\n"         "1. Add\n"         "2. Subtract\n"         "3. Multiply\n"         "4. Divide\n"         "5. Power\n")
    

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4, 5:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
elif select == 5:
    print(number_1, "^", number_2, "=",
                      power(number_1,number_2))
else:
	print("Invalid input")


# In[3]:


# Python code to demonstrate
# checking of element existence
# using loops and in

# Initializing list
test_list = [ 1, 6, 3, 5, 3, 4 ]

print("Checking if 4 exists in list ( using loop ) : ")

# Checking if 4 exists in list
# using loop
for i in test_list:
	if(i == 4) :
		print ("Element Exists")

print("Checking if 4 exists in list ( using in ) : ")

# Checking if 4 exists in list
# using in
if (4 in test_list):
	print ("Element Exists")


# In[4]:


# Let's create a dictionary, the functional way

# Create your dictionary class
class my_dictionary(dict):

	# __init__ function
	def __init__(self):
		self = dict()
		
	# Function to add key:value
	def add(self, key, value):
		self[key] = value

# Main Function
dict_obj = my_dictionary()

dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')

print(dict_obj)


# In[5]:


# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum
def returnSum(myDict):
	
	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)
	
	return final

# Driver Function
dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(dict))


# In[6]:


# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated

# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
		50, -20, 60, 60, -20, -20]
print (Repeat(list1))
	
# This code is contributed
# by Sandeep_anand


# In[7]:


# Python3 Program to check whether a
# given key already exists in a dictionary.

# Function to print sum
def checkKey(dict, key):
	
	if key in dict.keys():
		print("Present, ", end =" ")
		print("value =", dict[key])
	else:
		print("Not present")

# Driver Code
dict = {'a': 100, 'b':200, 'c':300}

key = 'b'
checkKey(dict, key)

key = 'w'
checkKey(dict, key)


# In[ ]:




