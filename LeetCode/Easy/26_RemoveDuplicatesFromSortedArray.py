"""
Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      k = 0
      uniqueArray = [0] * len(nums)
      for index in range(len(nums)-1):
         if(nums[index]!=nums[index+1]):
            uniqueArray[k] = nums[index]
            k+=1

      uniqueArray[k] = nums[len(nums)-1]
      k+=1
      for index in range(k):
        nums[index] = uniqueArray[index]
      return k
         
