age = int(input('enter age: '))

if(age>18):
    print('you can drive')
elif(age==18):
    print('lets schedule an interview')
elif(age==0):
    print('invalid age')
else:
    print('you cannot drive')