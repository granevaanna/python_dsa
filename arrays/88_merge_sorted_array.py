'''
LeetCode: 88
Title: Merge Sorted Array
Difficulty: Easy

Topics:
- Array
- Two pointers
- Sorting

Task:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Time Complexity: O(n+m)
Space Complexity: O(1)

Idea:
Создать указатель записи (right_write_idx) для записи элементов, начиная с конца массива.
Создать два указателя для чтения элементов массивов nums1 и nums2 (right_read_idx_for_nums1 и right_read_idx_for_nums2).
Идти в цикле while, пока оба указателя неотрицательны, и закончить, когда хотя бы один из них станет меньше нуля.
Внутри цикла сравнивать элементы двух массивов с индексами right_read_idx_for_nums1 и right_read_idx_for_nums2.
В nums1[right_write_idx] записывать больший из них, после чего сдвигать соответствующий указатель для чтения влево и
сдвинуть указатель для записи влево.
После завершения первого цикла, если в nums2 остались элементы, скопировать их в начало nums1.
Если же элементы остались только в nums1, ничего делать не нужно, так как они уже находятся на своих местах.

Date: 2026-07-02
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        right_write_idx = n+m-1
        right_read_idx_for_nums1 = m-1
        right_read_idx_for_nums2 = n-1
        while right_read_idx_for_nums1 >= 0 and right_read_idx_for_nums2 >= 0:
            if nums1[right_read_idx_for_nums1] > nums2[right_read_idx_for_nums2]:
                nums1[right_write_idx] = nums1[right_read_idx_for_nums1]
                right_read_idx_for_nums1 -= 1
            else:
                nums1[right_write_idx] = nums2[right_read_idx_for_nums2]
                right_read_idx_for_nums2 -= 1
            right_write_idx -= 1
        while right_read_idx_for_nums2 >= 0:
            nums1[right_write_idx] = nums2[right_read_idx_for_nums2]
            right_write_idx -= 1
            right_read_idx_for_nums2 -= 1



if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1 == [1,2,2,3,5,6]

    # Example 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1 == [1]

    # Example 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1 == [1]

    # Example 4 (my)
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1 == [1,2,3,4,5,6]