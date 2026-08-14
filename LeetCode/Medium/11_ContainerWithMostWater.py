"""
Problem Link : https://leetcode.com/problems/container-with-most-water/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
     low = 0
     high = len(height) - 1
     maxCapacity = 0
     while(low<high):
       capacity = (high - low ) * min(height[low], height[high])
       if(capacity > maxCapacity): maxCapacity = capacity
       if(height[low] < height[high]): low+=1
       else: high-=1
     return maxCapacity
