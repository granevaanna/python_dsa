'''
LeetCode: 53
Title: Maximum Subarray
Difficulty: Medium

Topics:
- Array
- Divide and Conquer

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

Time Complexity: O(n^2)
Space Complexity: O(1)

Idea:
Создать переменную max_sum и записать в нее первый элемент массива.
Для каждого индекса последовательно вычислять суммы всех подмассивов, начинающихся с этого индекса.
После каждого вычисления обновлять max_sum, если текущая сумма больше.
Вернуть max_sum.

Date: 2026-07-03
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(len(nums)):
            current_sum = nums[i]
            for j in range(i+1, len(nums)):
                current_sum += nums[j]
                max_sum = max(current_sum, max_sum)
        return max_sum

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