print("Welcome to the rollercoaster")
height = int(input("What is your height ?\n" ))
if(height >= 120):
  print("You can ride the rollercoaster")
  age = int (input("What is your age ?\n"))
  if(age < 12):
     print("You have to pay $5.")
  elif age <= 18 :  #here we can this condition >> elif(age > 12 and age <= 18):
     print("You have to pay $7.")
  else:
     print("You have to pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")