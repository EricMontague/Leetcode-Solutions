"""This file contains my solutions to Leetcode problem 896: Monotonic Array."""

# time complexity: O(n), where 'n' is the number of elements in the array
# space complexity: O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = False
        isDecreasing = False
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                isIncreasing = True
            elif nums[index] < nums[index - 1]:
                isDecreasing = True
            if isIncreasing and isDecreasing:
                return False
        return True


# Alternative solution
# time complexity: O(n), where 'n' is the number of elements in the array
# space complexity: O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        for index in range(len(nums) - 1):
            newDirection = self.calcDirection(nums[index + 1], nums[index])
            if direction == 0:
                direction = newDirection
            else:
                if direction > 0 and newDirection < 0:
                    return False
                if direction < 0 and newDirection > 0:
                    return False
        return True

    def calcDirection(self, num1, num2):
        if num1 - num2 == 0:
            direction = 0
        elif num1 - num2 > 0:
            direction = 1
        else:
            direction = -1
        return direction

