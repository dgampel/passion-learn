def merge_sort2(arr):

# step 1: split list into groups recursively until one element per group
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        #recursion
        merge_sort2(left)
        merge_sort2(right)

        i=0                             # left half
        j=0                             # right half
        k=0                             # main/new list

# step 2: compare each element and then group them

        while i < len(left) and j < len(right):
            if left[i] < right[j]:      # element in left list is smaller
                arr[k] = left[i]        # copy left element to new list k
                i = i+1                 # move left list over to next element
            else:                       # element in right is smaller
                arr[k] = right[j]       # copy right element to new list k
                j = j+1                 # move right list over to next element
            k = k+1                     # move new list over to next element

# step 3 (i think): repeat step 2 until whole list is merged and sorted
        while i < len(left):            # don't understand 
            arr[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):           # don't understand
            arr[k] = right[j]
            j = j+1
            k = k+1

arr = [17,45,6,24,1,150,36,80,16]
merge_sort2(arr)
print(arr)

