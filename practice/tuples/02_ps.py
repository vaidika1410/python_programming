# convert a tuple to a list, change its first element and convert it back to the tuple

coordinates = (10, 20)

list_of_coordinates = list(coordinates)

print(list_of_coordinates)
list_of_coordinates[0] = 50
print(list_of_coordinates)

# here coordinates variable point to the tuple(list_of_coordinates), instead of the old coordinates variable value 
coordinates = tuple(list_of_coordinates)
print(coordinates)