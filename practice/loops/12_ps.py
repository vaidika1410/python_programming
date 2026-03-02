# print numbers from 1 to 10 but stop the loop if the number is 7

for i in range(1,11):
    if(i == 7):
        break
    print(i)

# print numbers from 1 to 10 skipping number 5

for i in range(1, 11):
    if(i == 5):
        continue
    print(i)

# print numbers from 1 to 5 but does nothing for number 3

for i in range(1, 6):
    if i == 3:
        pass
    print(i)