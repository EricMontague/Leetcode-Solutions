"""This file contains my solution to Leetcode problem 3: Longest Substring without repeating characters."""


# time complexity: O(n), where 'n' is the number of characters in the string.
# space complexity: O(min(n, m)), where 'n' is the number of characters in the string
# and 'm' is the number of characters in the character set given (e.g. unicode, all lowercase letters etc.)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        lastSeen = {}
        start = 0         
        for end in range(len(s)):
            character = s[end]
            if character in lastSeen and lastSeen[character] >= start:
                start = lastSeen[character] + 1
            lastSeen[character] = end
            longest = max(longest, end - start + 1)
        return longest
      