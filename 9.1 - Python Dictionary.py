# {key : value}
# {"Bug" : "An error in a program that prevents the program from running as expected."}
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retriving new items from dictionary.
print(programming_dictionary["Bug"])
print("|")

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)
print("|")

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
print("|")

# Edit an item in a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
}
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])
print("|")

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
print("|")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])