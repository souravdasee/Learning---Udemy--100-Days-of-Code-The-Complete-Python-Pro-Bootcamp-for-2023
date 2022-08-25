import random

random_int = random.randint(1,10)   #random number from 1 to 10(including 1 & 10).
print(random_int)

rand_float = random.random()    #random number from 0 to 1 (excluding 1 ~ 0 to 0.999999999999)
print(rand_float)

rand_float_1 = random.random() * 5
print(rand_float_1)