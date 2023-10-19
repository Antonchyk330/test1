import random


a = 10
b = a + 0


mini = 30
maxi = 90


random_numbers = []


for _ in range(b):


    random_number = random.randint(mini, maxi)
    random_numbers.append(random_number)


print(random_numbers)
