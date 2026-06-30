'''
LeetCode: 1929
Title: Concatenation of Array
Difficulty: Easy

Topics:
- Array

Task:
Given an integer array nums of length n, you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]


Constraints:
n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000

Time Complexity: O(n)
Space Complexity: O(n)

Idea:
Создать новый массив ans, который в 2 раза больше исходного.
Пройти циклом по исходному массиву и записать каждый эллемент в ans[i] и ans[i+nums_len]

Date: 2026-06-30
'''

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0] * 2 * nums_len
        for i in range(nums_len):
            ans[i] = nums[i]
            ans[i + nums_len] = nums[i]
        return ans

    def getConcatenation_for_python(self, nums: List[int]) -> List[int]:
        return nums * 2

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1,2,1]
    result = solution.getConcatenation(nums)
    print(result)
    assert result == [1,2,1,1,2,1]

    # Example 2
    nums = [1,3,2,1]
    result = solution.getConcatenation(nums)
    print(result)
    assert result == [1,3,2,1,1,3,2,1]