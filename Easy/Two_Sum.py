"https://leetcode.com/problems/two-sum/description/"
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for c_1 in range(len(nums)):
            for c_2 in range(c_1+1,len(nums)):
                if nums[c_1]+nums[c_2]==target:
                    return(c_1,c_2)

