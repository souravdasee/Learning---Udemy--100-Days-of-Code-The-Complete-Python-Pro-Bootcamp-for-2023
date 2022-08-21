#Data Types

#String
a = "Hello"
b = "123" + "456"
print("a =", type(a))
print("b =", type(b))

#Integer
c = 123 + 456
d = 123_456 + 654_321
print("c =", type(c))
print("d =", type(d))

#Float
e = 3.14159
print("e =", type(e))

#Boolean
f = True
g = False
print("f =", type(f))
print("g =", type(g))


#Code_Challange

#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#-----------------------------------------------------------------------------------------------------------------------


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))