"""this file contains my solutions to Leetcode problem 2: Add Two Numbers."""



# time complexity: O(max(n,m)) where 'n' is the number of nodes in the first list and
# 'm' is the number of nodes in the second list
# space complexity : O(max(n, m))
class Solution:
    def addTwoNumbers(self, firstNumHead: ListNode, secondNumHead: ListNode) -> ListNode:
        sentinel = ListNode()
        sumTail = sentinel
        carry = 0
        currentFirst = firstNumHead
        currentSecond = secondNumHead
        while currentFirst or currentSecond:
            result = 0
            if currentFirst:
                result += currentFirst.val
                currentFirst = currentFirst.next
            if currentSecond:
                result += currentSecond.val
                currentSecond = currentSecond.next
            sum_ = result + carry
            sumTail.next = ListNode(sum_ % 10)
            sumTail = sumTail.next
            carry = sum_ // 10
            
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

class Solution3:
    def addTwoNumbers(self, firstNumHead: ListNode, secondNumHead: ListNode) -> ListNode:
        sum_ = self.addNumbers(firstNumHead, secondNumHead)
        return self.buildSumList(sum_)
    
    def addNumbers(self, firstNumHead, secondNumHead, base=10):
        sum_ = 0
        place = 0
        currentFirst = firstNumHead
        currentSecond = secondNumHead
        while currentFirst or currentSecond:
            if currentFirst and currentSecond:
                firstValue = currentFirst.val * (base ** place)
                secondValue = currentSecond.val * (base ** place)
                result = firstValue + secondValue
                currentFirst = currentFirst.next
                currentSecond = currentSecond.next
            elif currentFirst:
                result = currentFirst.val * (base ** place)
                currentFirst = currentFirst.next
            elif currentSecond:
                result = currentSecond.val * (base ** place)
                currentSecond = currentSecond.next
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