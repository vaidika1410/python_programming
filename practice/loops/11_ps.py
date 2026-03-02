# use a while loop to reverse a number

num = int(input('enter number: '))
sum = 0
temp = num
rem = 0

while temp > 0:
    rem = temp % 10
    temp = int(temp / 10)
    sum = sum * 10 + rem

print(sum)

# using string advanced slicing
# num = 442223
# print(int(str(num)[::-1]))
