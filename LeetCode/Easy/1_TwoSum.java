/**
 * Problem Link : https://leetcode.com/problems/two-sum/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] List = new int[2];
         int i=0; int j = i;
         while(i<nums.length-1){
            if(nums[i] + nums[j] == target){
                List[0] = i;
                List[1] = j;
            }
            if(j==nums.length-1){
                j = i+1;
                i++;
            }
            j++;
         }
         return List;
    }
}
