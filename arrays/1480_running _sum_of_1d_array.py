'''
LeetCode: 1480
Title: Running Sum of 1d Array
Difficulty: Easy

Topics:
- Array
- Prefix Sum

Task:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

Time Complexity: O(n)
Space Complexity: O(1)

Idea:
Проходим циклом по элементам массива начиная со второго и прибавляем к нему предыдущий.
Поняла, что можно использовать исходный массив, а не создавать новый.

Date: 2026-06-30
'''

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums



if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1,2,3,4]
    result = solution.running_sum(nums)
    print(result)
    assert result == [1, 3, 6, 10]

    # Example 2
    nums = nums = [1,1,1,1,1]
    result = solution.running_sum(nums)
    print(result)
    assert result == [1,2,3,4,5]

    # Example 3
    nums = [3,1,2,10,1]
    result = solution.running_sum(nums)
    print(result)
    assert result == [3,4,6,16,17]


