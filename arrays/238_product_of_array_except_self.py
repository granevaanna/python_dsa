'''
LeetCode: 238
Title: Product of Array Except Self
Difficulty: Medium

Topics:
- Array
- Prefix Sum

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

Time Complexity: O(n)
Space Complexity: O(n)

Idea:
Создать два массива prefix_product и sufix_product.
prefix_product[i] хранит произведение всех элементов слева от nums[i].
suffix_product[i] хранит произведение всех элементов справа от nums[i].
После этого вернуть массив [prefix_product[i] * suffix_product[i]], где i in range(len(nums)).
Вернуть массив result.

Date: 2026-07-06
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i+1]
        return [prefix_product[i] * suffix_product[i] for i in range(len(nums))]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1,2,3,4]
    result = solution.productExceptSelf(nums)
    print(result)
    assert result == [24,12,8,6]

    # Example 2
    nums = [-1,1,0,-3,3]
    result = solution.productExceptSelf(nums)
    print(result)
    assert result == [0,0,9,0,0]