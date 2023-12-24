"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

def maxArea(nums):
    lenNums = len(nums)
    multiple = []
    for i in range(lenNums):
        for j in range(lenNums):
            if nums[i] > nums[j] and j > i:
                multiple.append(nums[j]*(j-i))
            else:
                multiple.append(nums[i]*(j-i))
    return max(multiple)
print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))


#efficient code
def maxArea(nums):
    start = 0
    end = len(nums) - 1
    maxArea = 0
    while start != end:
        newArea = (end - start) * min(nums[start],nums[end])
        maxArea = max(maxArea,newArea)
        if nums[start] < nums[end]:
            start +=1
        else:
            end -=1
            
    
    return (maxArea)
