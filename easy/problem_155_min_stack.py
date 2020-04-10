"""This is my solution to Leetcode problem 155."""


#Overall time complexity of all operations are O(1)
#Overall space complexity of the solution is O(n)
class MinStackItem:
    
    def __init__(self, value, last_smallest_value):
        self.value = value
        self.last_smallest_value = last_smallest_value
        

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = [MinStackItem(None, float("inf"))]
        
    def push(self, x: int) -> None:
        if x < self.items[-1].last_smallest_value:
            item = MinStackItem(x, x)
        else:
            item = MinStackItem(x, self.items[-1].last_smallest_value)
        self.items.append(item)

    def pop(self) -> None:
        if len(self.items) > 1:
            self.items.pop()
    
    def top(self) -> int:
        return self.items[-1].value

    def getMin(self) -> int:
        return self.items[-1].last_smallest_value

