"""This file contains my solution for problem 125 - Valid Palindrome."""


# Overall time complexity: O(n), where 'n' is the number of characters in the string
# Overall space complexity is O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            if not s[low].isalnum():
                low += 1
            elif not s[high].isalnum():
                high -= 1
            else:
                if not s[low].lower() == s[high].lower():
                    return False
                low += 1
                high -= 1
        return True


# Explanation
# A word is a palindrome if it reads the same forwards and backwards.
# Based on the problem statemenet and examples given we are given a string that
# may consist of may possible types of characters, but that we should only consider
# alphanumeric characters when comparing characters in our algorithm and that our 
# comparisons should be case-insensitive. This means we can skip over spaces, 
# punctuation, and any other non-alhpanumeric characters and that a capital letter
# 'A' is considered to be the same as the lowercase 'a'.

# Approach - Two Pointer Technique:
# We can solve this problem using the two pointer technique. We create two variables,
# low and high, which are equal to the first and last index of the string, respectively.
# We will then start a while loop moving both pointers closer to each other until 
# both pointers meet or cross. 
# 
# If one of the pointers is pointing to a non-alphanumeric character, we can move that 
# pointer forward or backwards by 1, effectively skipping it, because we only want to 
# compare alphanumeric values. If both pointers point to alhpa-numeric characters we 
# do a case-insensitive comparison of both characters. Then, if they are both equal, 
# we simply move both pointers closer to each other, but if they are not equal, we 
# return False. Finally, if we complete our scan of the string and both pointers 
# have met or crossed, that means we have a valid palindrome and can return True

# Time complexity:
# The time complexity is O(n) because in the worst case the string is all 
# non-alphanumeric characters and we end up moving the low pointer through all 
# 'n' characters in the string. Another way to look at it is that even if the string 
# is a valid palindrome, we iterate at most n / 2 times before terminating the while 
# loop. Since we drop coefficients in Big O notation(1 / 2), this makes the time 
# complexity still O(n).

# Space complexity:
# Regardless of the size of the string the amount of size used remains constant. All we need
# is just two variables to store the pointers

