'''
LeetCode: 125
Title: Valid Palindrome
Difficulty: Easy

Topics:
- String
- Two Pointers

Task:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

Time Complexity: O(n)
Space Complexity: O(1)

Idea:
Далее создать два указателя для левого и правого индексов (left_idx и right_idx).
Идти двумя указателями навстречу друг другу, пока left_idx < right_idx.
Проверять, являются ли текущие элементы буквами или числами.
Если нет, то сдвигуть соответствующий указатель и начать цикл заново,
а если да, то сравнить их значения в нижнем регистре,
если они не совпадают, то сразу вернуть False.
Если совпали, то сдвинуть указатели left_idx и right_idx на один.
После прохождения цикла вернуть True, в таком случае все элементы совпали,
а значит строка является палиндромом.

Date: 2026-07-07
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        right_idx = len(s)-1
        while left_idx < right_idx:
            if not s[left_idx].isalnum():
                left_idx += 1
                continue
            if not s[right_idx].isalnum():
                right_idx -= 1
                continue
            if s[left_idx].lower() != s[right_idx].lower():
                return False
            left_idx += 1
            right_idx -= 1
        return True

    def display_result(self, s:str, result: bool):
        if result:
            print(f'"{s}"\nThis is a palindrome.')
        else:
            print(f'"{s}"\nThis isn\'t a palindrome.')

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    print('-------- Example 1 ------------')
    s = "A man, a plan, a canal: Panama"
    result = solution.isPalindrome(s)
    solution.display_result(s, result)
    assert result is True

    # Example 2
    print('-------- Example 2 ------------')
    s = "race a car"
    result = solution.isPalindrome(s)
    solution.display_result(s, result)
    assert result is False

    # Example 3
    print('-------- Example 3 ------------')
    s = " "
    result = solution.isPalindrome(s)
    solution.display_result(s, result)
    assert result is True

    # Example 4 (my)
    print('-------- Example 4 ------------')
    s = "0P"
    result = solution.isPalindrome(s)
    solution.display_result(s, result)
    assert result is False