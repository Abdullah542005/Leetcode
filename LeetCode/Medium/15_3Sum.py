"""
Problem Link : https://leetcode.com/problems/3sum/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
      nums.sort()
      result = []
      for index, target in enumerate(nums):
        if(index!=0 and target == nums[index-1]): continue
        start = (index + 1)  if index < (len(nums) - 1) else len(nums)-1
        end = len(nums)-1
        while(end>start):
          if((target + nums[start] + nums[end]) == 0):
             result.append([target, nums[start], nums[end]])
             while start < end and nums[start] == nums[start + 1]:
              start += 1
             while start < end and nums[end] == nums[end - 1]:
              end -= 1
             start+=1
             end-=1
          elif ((target + nums[start] + nums[end]) < 0):
             start+=1
          else:
            end-=1
      return result
