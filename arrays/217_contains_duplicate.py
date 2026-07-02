'''
LeetCode: 217
Title: Contains Duplicate
Difficulty: Easy

Topics:
- Array
- Hash Set

Task:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

Time Complexity: O(n)
Space Complexity: O(n)

Idea:
Создать множество seen_nums для записи уникальных элементов.
Пройти циклом по исходному массиву nums.
Если текущий элемент есть в множестве, то возвращаем True (значит этот элемент уже встречался).
Если элемента нет в множестве, то добавляем его.
После цикла возвращаем False, на тот случай, если исходный массив без дубликатов.

Date: 2026-07-02
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            seen_nums.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1,2,3,1]
    result = solution.containsDuplicate(nums)
    print(result)
    assert result == True

    # Example 2
    nums = [1,2,3,4]
    result = solution.containsDuplicate(nums)
    print(result)
    assert result == False

    # Example 3
    nums = [1,1,1,3,3,4,3,2,4,2]
    result = solution.containsDuplicate(nums)
    print(result)
    assert result == True