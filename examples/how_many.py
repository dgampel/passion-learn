nums = [1,2,0]	
howmany = 1

nums.sort()
for howmany in range(len(nums)):
    if nums.count(howmany) == 0:
        print(howmany)
        continue
    if nums.count(howmany) >= 1:
        howmany + 1

