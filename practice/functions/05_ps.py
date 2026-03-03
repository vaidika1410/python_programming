# a lambda function to print square of numbers in a list

nums = [1, 2, 3, 4, 5]

square = lambda num: num*num 

print(list(map(square, nums)))