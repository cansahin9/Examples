# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

limit = 4000000

sum = 0
first = 1
second = 1
third = first + second

while third < limit:
    sum += third
    first = second + third
    second = third + first
    third = first + second

print(sum)