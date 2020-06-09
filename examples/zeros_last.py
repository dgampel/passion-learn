'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
def zeros(nums):
    j = 0
    for n in nums:
        if n!=0:
            nums[j] = n
            j += 1
    
    for i in range(j,len(nums)):
        nums[i] = 0

    return nums

arr = [0,1,0,0,0,2,0,3,4,5]
print(zeros(arr))
