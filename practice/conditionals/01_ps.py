# check whether the number input by the user is positive, negative or zero

num = int(input("enter a number: "))

if(num > 0):
    print("number", num, " is positive")
elif(num == 0):
    print("number is", num)
else:
    print("number", num, "is negative")