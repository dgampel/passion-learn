def num_sort(list_array):
    for j in range(1,len(list_array)):
        key = list_array[j]

        i = j - 1
        while (i >= 0 and list_array[i] > key):
            list_array[i+1] = list_array[i]
            i = i - 1
            print(i)
        list_array[i+1] = key
    return list_array

list_array = [9,8,7,6]

print(num_sort(list_array))

