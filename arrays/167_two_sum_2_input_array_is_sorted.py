'''
LeetCode: 167
Title: Two Sum II - Input Array Is Sorted
Difficulty: Medium

Topics:
- Array
- Two Pointers
- Greedy

Task:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2,
each incremented by one, as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution.
You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

Time Complexity: O(n)
Space Complexity: O(1)

Idea:
Создать два указателя left_idx и right_idx.
Проходить цикл while, пока left_idx меньше, чем right_idx.
В цикле вычислять сумму элементов под текущими указателями.
Если эта сумма равна target, то вернуть список: [left_idx + 1, right_idx + 1].
Если текущая сумма больше, чем target, то двигаем правый указатель,
если меньше, то двигаем левый указатель.
Мы можем так сделать, так как массив отсортирован и мы можем быть уверены,
что сдвинув правый указатель, сумма уменьшится,
а сдвинув левый - увеличится.
Также условие гарантируем, что обязательно такие числа будут,
поэтому можно не возвращать пустой массив, на случай если ничего не будет найдено.

Date: 2026-07-09
'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1
        while left_idx < right_idx:
            current_sum = numbers[left_idx] + numbers[right_idx]
            if current_sum == target:
                return [left_idx + 1, right_idx + 1]
            elif current_sum > target:
                right_idx -= 1
            else:
                left_idx += 1

if __name__ == "__main__":
    solution = Solution()

    def run_test(numbers: List[int], target: int, expected: List[int]):
        result = solution.twoSum(numbers, target)
        print(f"Result: {result}")
        assert result == expected

    run_test([2,7,11,15], 9, [1, 2])
    run_test([2,3,4], 6, [1, 3])
    run_test([-1,0], -1, [1, 2])
