# the function takes a list and a target
def twoSum(nums, target):
    #  len(li) is used to find the length of the given list. Now, when you apply the range function upon len(li) as range(len(li)) it creates a squence of numbers from 0 up to len(li)-1. These numbers can then be used as indices of the given list such that you can access each item in the list using its index with the help of a for loop.
    for i in range(len(nums)):
        # print(i)
    # increment the first index and moves to the next item 
        for j in range(i+1,len(nums)):
            # print(j)
            if nums[i]+nums[j] == target:
              return(i,j)       

nums = [2,7,11,15]
print(twoSum(nums, 9))