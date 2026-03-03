text = " i love python programming "

print(text.strip())
print(text.title())


# counting the number of times o occurs

count = 0

for i in range(0, len(text)):
    if(text[i] == 'o'):
        count+=1
    else:
        continue

print("The number of times 'o' appears: ", count)

print(text.count('o'))