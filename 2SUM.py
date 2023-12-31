# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

"Example 1: \
Input: nums = [2,7,11,15], target = 9 \
Output: [0,1] \
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

#   WRONG

        for i in nums:
            for j in nums:
                if nums.index(i) != nums.index(j) and i + j == target:
                    return [nums.index(i), nums.index(j)]
                else:
                    continue

#   CORRECT

        a = 1
        for i in range(len(nums)):
            for j in range(a,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
            a += 1