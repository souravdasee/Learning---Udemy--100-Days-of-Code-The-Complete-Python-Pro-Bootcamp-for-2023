#Code_Challenge

#Write a program that works out whether if a given number is an odd or even number.

# >>>>>>>>>>>>>>>>Hint<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# All even numbers can be divided by 2 with 0 remainder.
# Try some using the modulo with some odd numbers e.g.
# 3 % 2
# 5 % 2
# 7 % 2
# Then try using the modulo with some even numbers e.g.
# 4 % 2
# 6 % 2
# 8 % 2
# See what's in common each time.
#----------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number%2:
    print("This is an odd number.")
else:
    print("This is an even number.")