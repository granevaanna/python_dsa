'''
LeetCode: 27
Title: Remove Element
Difficulty: Easy

Topics:
- Array
- Two pointers

Task:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

Time Complexity: O(n)
Space Complexity: O(1)

Idea:
Создать два указателя: left_idx и right_idx.
Продолжать выполнять цикл, пока left_idx не превышает right_idx.
Если nums[left_idx] не равно val, то двигаем левый указатель на один вправо,
а если равно, то проверяем nums[right_idx] на равенство с val и, если они не равны, то меняем местами nums[left_idx] и nums[right_idx],
после чего сдвигаем оба указателя.
А если nums[right_idx] было равно val, то просто сдвигаем правый указатель на один влево.
Таким образом, по ходу цикла мы "перебрасываем" все элементы равные val в конец массива.

Сложность:
Перепробовала много вариантов прежде, чем пришла к идее с двумя указателями.
Также после решения нашла другое хорошее решение на YouTube. Его преимущество в том,
что здесь не меняется порядок элементов массива и оно является более универсальным.
Но так как для решения этой задачи порядок элементов не имеет значения, оставляю свое решение как основное.

Date: 2026-07-01
'''

from typing import List

class Solution:
   def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx <= right_idx:
            if nums[left_idx] != val:
                k += 1
                left_idx += 1
            else:
                if nums[right_idx] != val:
                    k += 1
                    nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                    left_idx += 1
                # nums[right_idx] = "_"
                right_idx -= 1
        return k

    # ---- Alternative solution ----
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     write = 0
    #
    #     for read in range(len(nums)):
    #         if nums[read] != val:
    #             nums[write] = nums[read]
    #             write += 1
    #
    #     return write



if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3,2,2,3]
    val = 3
    result = solution.removeElement(nums, val)
    print(result)
    print(nums)
    assert result == 2
    assert sorted(nums[:result]) == [2, 2]

    # Example 2
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = solution.removeElement(nums, val)
    print(result)
    print(nums)
    assert result == 5
    assert sorted(nums[:result]) == [0, 0, 1, 3, 4]