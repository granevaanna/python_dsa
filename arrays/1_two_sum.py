'''
LeetCode: 1
Title: Two Sum
Difficulty: Easy

Topics:
- Array
- Hash Table

Task:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Time Complexity: O(n^2)
Space Complexity: O(1)

Idea:
Идти циклом по массиву и для каждого элемента перебирать оставшиеся элементы массива.
Как только сумма равно target, возвращает их индексы.

Сложность:
Time Complexity: O(n^2), надо подумать как это оптимизировать.

Date: 2026-07-02
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [2,7,11,15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)
    assert sorted(result) == [0,1]

    # Example 2
    nums = [3,2,4]
    target = 6
    result = solution.twoSum(nums, target)
    print(result)
    assert sorted(result) == [1, 2]

    # Example 3
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print(result)
    assert sorted(result) == [0, 1]