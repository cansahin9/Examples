# What is the largest prime factor of the number 600851475143 ?

num = 600851475143

for i in range(1, num+1):
    if num % i == 0:
        num = num/i
        print(num)
