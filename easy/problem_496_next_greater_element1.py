"""This is my solution to Leetcode problem 496: Next Greater Element 1."""


# time complexity: O(n + m), where  'n' is nums1 and 'm' is nums2
# space complexity: O(n + m), where  'n' is nums1 and 'm' is nums2

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elements = self.findnextGreaterElements(nums2)
        return self.getElements(nums1, elements)
    
    def findnextGreaterElements(self, nums2):
        elements = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                element = stack.pop()
                elements[element] = num
            stack.append(num)
        return elements
    
    def getElements(self, nums1, elements):
        output = [
            elements.get(num, -1) for num in nums1
        ]
        return output