# count how many vowels are there in a given string

string = 'Python is fun'
count = 0

for i in range(0, len(string)):
    match string[i]:
        case 'a':
            count+=1
        case 'e':
            count+=1
        case 'i':
            count+=1
        case 'o':
            count+=1
        case 'u':
            count+=1

print(count)