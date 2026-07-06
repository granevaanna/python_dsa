'''
LeetCode: 53
Title: Maximum Subarray
Difficulty: Medium

Topics:
- Array
- Divide and Conquer
- Dynamic Programming

Task:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Time Complexity: O(n)
Space Complexity: O(1)

Idea:
Алгоритм Канаде.
Создать переменные global_max и current_max, записать в них первый элемент массива.
Идти циклом по массиву, начиная со второго элемента:
В current_max записывать большее число из текущего элемента и суммы текущего элемента и current_max
(чтобы определить, что выгоднее: начать считать сумму с нового элемента или продолжить предыдущую).
В global_max записать значение current_max, если оно больше чем то, что было записано в global_max.
После завершения цикла вернуть global_max.

Date: 2026-07-03
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            global_max = max(current_max, global_max)
        return global_max

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solution.maxSubArray(nums)
    print(result)
    assert result == 6

    # Example 2
    nums = [1]
    result = solution.maxSubArray(nums)
    print(result)
    assert result == 1

    # Example 3
    nums = [5,4,-1,7,8]
    result = solution.maxSubArray(nums)
    print(result)
    assert result == 23