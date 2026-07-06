'''
LeetCode: 169
Title: Majority Element
Difficulty: Easy

Topics:
- Array
- Hash TableGiven an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.

Follow-up: Could you solve the problem in linear time and in O(1) space?

Time Complexity: O(n)
Space Complexity: O(n)

Idea:
Создать словарь nums_count, где ключ - число из массива, значение - количество его вхождений в массив.
Пройти циклом по массиву, создавать ключ с текущим элементом, если его нет, а если есть, то добавлять один к значению.
После цикла вернуть ключ из словаря с наибольшмм значением.

Date: 2026-07-06
'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        return max(nums_count, key=nums_count.get)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3,2,3]
    result = solution.majorityElement(nums)
    print(result)
    # assert result == 3

    # Example 2
    nums = [2,2,1,1,1,2,2]
    result = solution.majorityElement(nums)
    print(result)
    # assert result == 2