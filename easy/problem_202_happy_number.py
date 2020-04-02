"""These are my solutions to Leetcode problem 202."""


#A more space efficient solution
#Overall time complexity: O(n + k), where "n" is the number of integers
#seen before you reach 1 or find out that you're in a cycle. "k" is the total 
#number of digits in all of the integers until you either reach 1 or find a cycle.

#Overall space complexity: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            slow = self.sum_of_square_of_digits(slow)
            for num in range(2):
                fast = self.sum_of_square_of_digits(fast)
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
        
    def sum_of_square_of_digits(self, n):
        running_sum = 0
        while n != 0:
            digit = n % 10
            running_sum += digit ** 2
            n = n // 10
        return running_sum
            
        

#Overall time complexity: O(n + k), where "n" is the number of integers
#seen before you reach 1 or find out that you're in a cycle. "k" is the total 
#number of digits in all of the integers until you either reach 1 or find a cycle.

#Overall space complexity: O(n)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.sum_of_square_of_digits(n)
        return True
        
    def sum_of_square_of_digits(self, n):
        running_sum = 0
        while n != 0:
            digit = n % 10
            running_sum += digit ** 2
            n = n // 10
        return running_sum




            
        