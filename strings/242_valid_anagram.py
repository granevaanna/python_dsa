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
Если длины строк равны, то создать два словаря для каждой строки,
в которых в качестве ключа хранить буквы, а в качестве значения - количество букв в слове (эту логику вынести в отдельную функцию: char_counts).
Если словари равны, строки являются анаграммами.

Date: 2026-07-02
'''


class Solution:
    def char_counts(self, s: str) -> dict[str, int]:
        s_counts = {}
        for s_char in s:
            if s_char in s_counts:
                s_counts[s_char] += 1
            else:
                s_counts[s_char] = 1
        return s_counts

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = self.char_counts(s)
        t_counts = self.char_counts(t)
        return s_counts == t_counts



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