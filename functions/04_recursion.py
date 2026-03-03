# fibonacci series

def fib(n):
    # base case
    if (n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1)

print(fib(5))

# printing the series till n

for i in range(0, 10):
    print(fib(i))