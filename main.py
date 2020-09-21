# Chapter 4 Demo

"""
FOR LOOPS
Work with any 'Sequence' structure in Python

Example
	for letter in word:
	    print(letter)


"""

# Accessing the built-in range function
# syntax for the function, range(start, stop, step)

# Example 1
# print("\nBasic loop structure")
# for i in range(10):  # Range with a single parameter starts at 0 inclusively up to but not including the number passed
#     print(i, end=" ")  # the end of the range in this case '10'  is exclusive
#
#
# # Example 2
# print("\n\nCounting forwards w/ increment")
# for i in range(0, 50, 5):  # Sets up your loop to loop through 0-49 includes 0 but excludes 50
#     print(i, end=" ")  # The 3rd parameter passed controls the 'Count by/ or step' in this example 5
#
#
# # Example 3
# # We can also count backwards utilizing the range() function
# # Passing a negative number as the third argument is how this is done
# # It looks like this
#
# print("\n\nCounting backwards w/ an increment")
# for i in range(20, 0, -2):
#     print(i, end=" ")



"""
SEQUENCE OPERATORS 

Sequence operators can tell you information about a sequence
Here we will look at two important opeators:
len(), and 'in'

"""
# The len() will return the length of a sequence structure (how many elements does it contain)
# The 'in' operator can be used to find elements in a sequence

# Example 1
# Demonstrates the for loop with a string

# word = input("Enter a word: ")
#
# print("\nHere's each letter in your word:")
# for letter in word:
#     print(letter)
#

# Example 2
# Demonstrates the len() function and the in operator
#
# message = input("Enter a message: ")
#
# print("\nThe length of your message is:", len(message))
#
# print("\nThe most common letter in the English language, 'e',")
# if "e" in message:
#     print("is in your message.")
# else:
#     print("is not in your message.")




"""
SEQUENTIAL vs RANDOM ACCESS

Previously we looked at accessing each element of a sequence in order, or sequentially
We can also access each element of a sequence directly without traversing through the sequence
This is known as 'Random Access' Python sequence structures support Random Access
This is acomplished using an elements 'index' or position

"""

# Example 1
# import random #Calling the Random class gives us acces to the random methods
#
# word = "index" #Setting the value of the word variable
#
# high = len(word) #Using the len() function to automatically get the length of the string/ sequence
#                  #starts from left to right or index position [0] to [4]
#
# low = -len(word) #Using the reverse direction to find the length of word from right to left
#                  #index positions [-5] to [-1]
#
#
# for i in range(10): #Set the number of steps for the loop to run 10 times [0-9]
#     position = random.randrange(low, high) # Chooses a random index position
#                                             # anywhere between (-5 and -1) & (0 to 4) for added variation
#                                             # The first letter in 'word' is both index position [0] & [-5]
#
#     print("You are at index [", position, "] in 'word' \t", " the letter is: ", word[position])
#         #The statement above first prints the randomly chosen index position
#         # then the letter associated with that position



"""
MUTABILITY 

Some sequence structures can be changed while some can not
Structures that allow changes are said to be 'Mutable' 
Those that do not support this are 'Immutable' for example strings are Immutable

"""

# Example 1
# Demo Mutability vs Immutability

#Strings are immtable
#Lists are mutable

                    #IMMUTABLE
# print("\n\n-----------------------------------------IMMUTABLE-----------------------------------------------------------\n\n")
# word = "Hello World!" #This sets 'word' equal to the string value on the right of the '=' sign
# #word[0] = "Y"  #Uncomment this line to mutate the value at index position 0 'H' to the value 'Y'
#                 #You will notice an error notifying you this is not allowed
#
#
#
# word = "Yellow World!" # Here we assigned a new value to the 'word' variable which is allowed
#
# print(word)
#
# print("\n\n-------------------------------------------MUTABLE-----------------------------------------------------------\n\n")
#
#
#
#                     #MUTABLE
#
# myList = [ "car", "boat", "motorcycle"]
# print("myLinst currently has the values: \t", myList, "\n")
#
# myList[0] = "plane" #Here we mutated the value at index position [0] to the value 'plane'
#                     #because lists are mutable
#
# print("Here we have replaced index position 0, 'car',  with the value 'plane' \t", myList)



# Example 2
# No Vowels
# Demonstrates creating new strings with a for loop

# message = input("Enter a message: ")
# new_message = ""
# VOWELS = "aeiou"
#
# print()
# for letter in message:
#     if letter.lower() not in VOWELS:
#         new_message += letter
#         print("A new string has been created:", new_message)
#
# print("\nYour message without vowels is:", new_message)



"""
SLICING 

We used indexing to select individual elements from a sequence
We use 'Slicing' to select multiple elements from a sequence 
This works much the same way 'Indexing' does, except we supply both a start and end position

Slicing 'Cheat Sheet' 

 0   1   2   3   4   5
 +---+---+---+---+---+ 
 | p | i | z | z | a | 
 +---+---+---+---+---+ 
-5  -4  -3  -2  -1
"""

# Example 1
# Demonstrates string slicing

# word = "pizza"
#
# print("Enter the beginning and ending index for your slice of 'pizza'.")
# print("Press the enter key at 'Begin' to exit.")
#
# # Start has no value
# start = None
# while start != "": # Compares value of start to an empty string
#     start = (input("\nStart: "))
#
#     if start:
#         start = int(start) # Casts start to an int
#
#         finish = int(input("Finish: "))
#
#         print("word[", start, ":", finish, "] is", end=" ")
#         print(word[start:finish])



"""
TUPLES 

Tuples are another sequence structure in Python
Tuples work much the same as lists with one major difference
Tuples are 'Immutable' where 'Lists' are 'Mutable' 
"""

# Example 1
# Hero's Inventory
# Demonstrates tuple creation

# # create an empty tuple
# inventory = ()
#
# # treat the tuple as a condition
# if not inventory: # If inventory has no items
#     print("You are empty-handed.")
#
# input("\nPress the enter key to continue.")
#
# # create a tuple with some items
# inventory = ("sword",
#              "armor",
#              "shield",
#              "healing potion")
#
# # print the tuple
# print("\nThe tuple inventory is:")
# print(inventory)
#
# # print each element in the tuple
# print("\nYour items:")
# for item in inventory:
#     print(item)


# Example 2
# Hero's Inventory 2.0
# Demonstrates tuples

# create a tuple with some items and display with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print("Your items:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")

# get the length of a tuple
print("You have", len(inventory), "items in your possession.")

input("\nPress the enter key to continue.")

# test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# display a slice
print("You have", len(inventory), "items in your possession.")
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

# concatenate two tuples
chest = ("gold", "gems")
print("\n\nYou find a chest.  It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

