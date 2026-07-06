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
Space Complexity: O(1)

Idea:
Создать переменную candidate, куда записать первый элемент массива и count, куда присвоить 1.
Идти циклом по массиву, начиная со второго элемента массива.
В цикле: если текущий элемент равен значению candidate, то увеличиваем счетчик count на 1,
а если не равен, то отнимаем от счетчика count 1.
Если после этого счетчик count стал равен 0, заменяем candidate на текущий элемент,
а счетчику count присваиваем значение 1.
После прохождения цикла возвращаем значение candidate

Это алгоритм большинства голосов Бойера-Мура, но для этого алгоритма нужно делать еще один проход,
чтобы убедиться, что majority element действительно встречается n/2 раза.
Например, для nums = [1,2,3,4], текущий алгоритм вернет 4, хотя большинства нет.
(здесь это можно не делать, так как условие гарантирует, что подходящий элемент будет в массиве).

Date: 2026-07-06
'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                if count ==0:
                    candidate = nums[i]
                    count = 1
        return candidate

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