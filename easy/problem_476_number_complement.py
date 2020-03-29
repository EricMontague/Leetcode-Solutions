"""These are my solutions to problem 476."""

#Overall time complexity: O(log n), where "n" is the given integer
#Over space complexity: O(1)
class Solution:
    def findComplement(self, num: int) -> int:
        place = 0
        complement = 0
        while num > 0:
            remainder = num % 2
            if remainder == 0:
                complement += 2 ** place
            place += 1
            num = num // 2
        return complement


#Explanation: You can conver the given integer to binary and build its complement
#at the same time. After you find the remainder of "num", if it is equal to 1,
#then in the number's complement, this would be 0 and vice versa. Since this process
#builds the binary number from right to left, you can build the decimal number as you
#go. If the remainder equals 0, add 2 to the power of the place you are in since the
#complement would be 1 * 2 ** place. If it is 1, you don't have to do anything since the
#complementing digit would be 0 and you would just end up adding zero.

#This process takes O(logn + 1) time, but after you drop the 1, it becomes O(log n)
   