'''
LeetCode: 242
Title: Valid Anagram
Difficulty: Easy

Topics:
- Hash Table
- String

Task:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Time Complexity: O(n)
Space Complexity: O(n)

Idea:
Проверить, равны ли длины строк. Если нет, то сразу вернуть False.
Если длины строк равны, то создать словарь для первой строки,
в котором в качестве ключа хранить буквы, а в качестве значения - количество букв в строке.
Далее пройти циклом по второй строке. Если текущей буквы нет в словаре, то сразу возвращаем False.
Если текущая буква уже есть в словаре, то от значения отнимаем 1.
Когда значение равно 0, то удаляем пару ключ-значение из словаря.
Возвращаем True, если словарь после прохождения цикла пуст.

Date: 2026-07-02
'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = {}
        for s_char in s:
            s_counts[s_char] = s_counts.get(s_char, 0) + 1
        for t_char in t:
            if t_char not in s_counts:
                return False
            s_counts[t_char] -= 1
            if s_counts[t_char] == 0:
                del s_counts[t_char]
        return not s_counts

    # Pythonic solution using Counter
    def isAnagram_pythonic(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)
    assert result is True

    # Example 2
    s = "rat"
    t = "car"
    result = solution.isAnagram(s, t)
    print(result)
    assert result is False

    # Example 3
    s = "rddd"
    t = "ll"
    result = solution.isAnagram(s, t)
    print(result)
    assert result is False