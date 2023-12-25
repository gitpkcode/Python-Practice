"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

"""
def threeSumClosest(nums, target) -> int:
    nums.sort()
    closest = sum(nums[:3])
    if closest >= target:
        return closest
    closest = sum(nums[-3:])
    if closest <= target:
        return closest
    
    for left in range(len(nums) - 2):
        mid, right = left+1, len(nums)-1
        
        while mid<right:
            curr_sum = nums[left] + nums[mid] + nums[right]
            
            if abs(target - curr_sum) < abs(target - closest):
                closest = curr_sum
            elif curr_sum < target:
                mid +=1
            else:
                right -=1
                
    return closest

print(threeSumClosest([-1,2,1,-4],1))
print(threeSumClosest([0,0,0],1))