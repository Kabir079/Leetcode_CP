#Question : 
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

# Method 1 : 
# Description : Time complexicity : o(n square) 
# Reason : Cuz we iterate many times , that why it becomes n square

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        y = 0
        while(i<l): 
            if (nums[y] + nums[y+1] == target) :
                j = nums[y]
                k = nums[y+1]
                b = []
                b.append(nums.index(j))
                b.append(nums.index(k))
                return b
                
# Method 2 :
# Description : Time complexicity : o
# Reason : Because we use simple math logic and HeapMap as application and iterate less in comoarision to the 1st METHOD , therefore it is Linear time complexity.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index 
        
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap: 
                return [prevMap[diff], i]
            prevMap[n] = i 
        return 
  
