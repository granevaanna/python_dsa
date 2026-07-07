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
Space Complexity: O(1)

Idea:
Пройти циклом по списку nums.
Так как все числа из списка лежат в диапазоне от 1 до len(nums),
а индексы у этих чисел идут от 0 до (len(nums) - 1),
мы можем использовать индексы, чтобы помечать какие числа встречались в списке.
Для каждого элемента num перейти к индексу (abs(num) - 1) и сделать число по этому индексу отрицательным.
Элемент берем по модулю, так как некоторые числа могли быть уже помечены ранее и на данный момент могут быть отрицательными,
а также от элемента отнимаем единицу, так как индексы нумеруются от 0 до (len(nums) - 1).
Перед изменением знака проверить, что число по этому индексу еще положительное (то есть не было помечено ранее).
Вернуть список индексов, добавив к ним 1, под которыми числа положительны (то есть не были помечены, а значит не встречались в списке).

Date: 2026-07-07
'''

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        return [i+1 for i, num in enumerate(nums) if num>0]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [4,3,2,7,8,2,3,1]
    result = solution.findDisappearedNumbers(nums)
    print(result)
    assert result == [5, 6]

    # Example 2
    nums = [1,1]
    result = solution.findDisappearedNumbers(nums)
    print(result)
    assert result == [2]