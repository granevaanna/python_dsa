'''
LeetCode: 448
Title: Find All Numbers Disappeared in an Array
Difficulty: Easy

Topics:
- Array
- Hash Table

Task:
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Time Complexity: O(n)
Space Complexity: O(n)

Idea:
Создать множество nums_sequence с числами от одного до len(nums).
Пройти циклом по списку nums и удалить каждый встретившийся элемент из множества nums_sequence.
Вернуть множество, преобразовав его в список.

Date: 2026-07-07
'''

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_sequence = set(range(1, len(nums) + 1))
        for num in nums:
            nums_sequence.discard(num)
        return list(nums_sequence)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [4,3,2,7,8,2,3,1]
    result = solution.findDisappearedNumbers(nums)
    print(result)
    assert sorted(result) == [5, 6]

    # Example 2
    nums = [1,1]
    result = solution.findDisappearedNumbers(nums)
    print(result)
    assert result == [2]