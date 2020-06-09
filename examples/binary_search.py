def binary_search(array,first,last,x):

    array.sort()

    if last >= 1:                   #base case
        middle = 1 + (last - 1) // 2 
    
        if array[middle] == x:      #if element is present at middle
            return middle

        if array[middle] > x:       #if element is in left half
            return binary_search(array,first,middle-1,x)

        else:                       #if element is in right half
            return binary_search(array,middle+1,last,x)

    else:                           #if element is not present in array
        return -1

array = [1, 21, 14, 3, 2, 18, 10, 3, 47, 7]  # test array
x = 10                              #test element

first = 0
last = len(array)                   

answer = binary_search(array,first,last,x)

if answer != -1:
    print("Element is present at index", str(answer))

else:
    print("Element is not present in array")
   

