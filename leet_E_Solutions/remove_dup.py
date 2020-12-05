"""
Given a sorted array nums, remove the duplicates 'in-place' such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

def remove_Dups_In_place(nums):
    if len(nums) == 0 :
        return False

    # Make a copy of list to meet in-place requirement subsequently removing dups with set()
    nums[:]= set(nums)
    counter = 1
    

    #Manually sort list 
    for idx in range(len(nums)):
        # Ensure val at index is greater than index - 1  
        if nums[idx] < nums[idx-1]:
            # Swape values at index 
            nums[idx], nums[idx - 1]=  nums[idx - 1], nums[idx]
            print(str(counter) +"-->"+ str(nums))
            counter +=1

    # Sort list, then return len
    return len(nums)

remove_Dups_In_place([0,0,1,1,1,2,2,3,3,4])

'''
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the returned length.
'''

'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. 
It doesn't matter what values are set beyond the returned length.
'''