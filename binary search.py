

def binarySearch(array, key):
    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:
        mid_index = int((min_index + max_index) / 2)


        if key == array[mid_index]:
            return mid_index

        elif key < array[mid_index]:
            max_index = mid_index - 1

        else:
            min_index = mid_index + 1

    return -1

run = True
while run:

    my_list = [1, 2, 47, 4, 65, 16, 7, 8, -4, 3]
    my_list = sorted(my_list)

    value = input("Enter the value:")

    if value == 'exit':
        break

    intValue = int(value)
    location = binarySearch(my_list, intValue)

    if location == -1:
        print("The value not found")

    else:
        print("The value is in location", location)