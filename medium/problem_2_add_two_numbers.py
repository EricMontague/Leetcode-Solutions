"""this file contains my solutions to Leetcode problem 2: Add Two Numbers."""



# time complexity: O(max(n,m)) where 'n' is the number of nodes in the first list and
# 'm' is the number of nodes in the second list
# space complexity : O(max(n, m))
class Solution:
    def addTwoNumbers(self, firstNumHead: ListNode, secondNumHead: ListNode) -> ListNode:
        sentinel = ListNode()
        sumTail = sentinel
        carry = 0
        while firstNumHead or secondNumHead:
            if firstNumHead and secondNumHead:
                result = firstNumHead.val + secondNumHead.val
                firstNumHead = firstNumHead.next
                secondNumHead = secondNumHead.next
            elif firstNumHead:
                result = firstNumHead.val
                firstNumHead = firstNumHead.next
            elif secondNumHead:
                result = secondNumHead.val
                secondNumHead = secondNumHead.next
            sumTail.next = ListNode((result + carry) % 10)
            sumTail = sumTail.next
            if result + carry > 9:
                carry = (result + carry) // 10
            else:
                carry = 0
        if carry > 0:
            sumTail.next = ListNode(carry)
        return sentinel.next
            
        

# Two pass solution
# time complexity: O(n + m)
# space complexity: O(max(n,m))
class Solution2:
    def addTwoNumbers(self, firstNumHead: ListNode, secondNumHead: ListNode) -> ListNode:
        firstNum = self.extractNum(firstNumHead)
        secondNum = self.extractNum(secondNumHead)
        return self.buildSumList(firstNum + secondNum)
    
    def extractNum(self, head, base=10):
        num = 0
        place = 0
        current = head
        while current:
            num += current.val * (base ** place)
            place += 1
            current = current.next
        return num
    
    def buildSumList(self, sum_, base=10):
        if sum_ == 0:
            return ListNode(sum_)
        sentinel = ListNode()
        tail = sentinel
        while sum_ > 0:
            lastDigit = sum_ % base
            sum_ = sum_ // 10
            tail.next = ListNode(lastDigit)
            tail = tail.next
        return sentinel.next



# Converted the two pass solution into one pass
# time complexity: O(max(n, m))
# space complexity: O(max(n, m))

class Solution:
    def addTwoNumbers(self, firstNumHead: ListNode, secondNumHead: ListNode) -> ListNode:
        sum_ = self.addNumbers(firstNumHead, secondNumHead)
        return self.buildSumList(sum_)
    
    def addNumbers(self, firstNumHead, secondNumHead, base=10):
        sum_ = 0
        place = 0
        while firstNumHead or secondNumHead:
            if firstNumHead and secondNumHead:
                firstValue = firstNumHead.val * (base ** place)
                secondValue = secondNumHead.val * (base ** place)
                result = firstValue + secondValue
                firstNumHead = firstNumHead.next
                secondNumHead = secondNumHead.next
            elif firstNumHead:
                result = firstNumHead.val * (base ** place)
                firstNumHead = firstNumHead.next
            elif secondNumHead:
                result = secondNumHead.val * (base ** place)
                secondNumHead = secondNumHead.next
            sum_ += result
            place += 1
        return sum_
    
    def buildSumList(self, sum_, base=10):
        if sum_ == 0:
            return ListNode(sum_)
        sentinel = ListNode()
        tail = sentinel
        while sum_ > 0:
            lastDigit = sum_ % base
            sum_ = sum_ // 10
            tail.next = ListNode(lastDigit)
            tail = tail.next
        return sentinel.next