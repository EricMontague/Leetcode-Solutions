"""This is my solution to Leetcode problem 146: LRU Cache."""


class DLinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = DLinkedListNode(None, None)
        self.tail = DLinkedListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def push_head(self, item):
        item.next = self.head.next
        self.head.next = item
        item.next.prev = item
        item.prev = self.head
        
    def pop_tail(self):
        tail = self.tail.prev
        self.remove(tail)
        return tail
        
    def remove(self, item):
        item.prev.next = item.next
        item.next.prev = item.prev
    
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_items = 0
        self.linked_list = DoublyLinkedList()
        self.items = {}

    def get(self, key: int) -> int:
        if not self.exists(key):
            return -1
        item = self.items[key]
        self.move_to_front(item)
        return item.value
        
    def put(self, key: int, value: int) -> None:
        if not self.exists(key):
            if self.is_full():
                self.evict()
                self.num_items -= 1
            item = DLinkedListNode(key, value)
            self.items[key] = item
            self.linked_list.push_head(item)
            self.num_items += 1
        else:
            item = self.items[key]
            item.value = value
            self.move_to_front(item)
            
    def exists(self, key):
        return self.items.get(key) is not None
    
    def is_full(self):
        return self.num_items == self.capacity
    
    def move_to_front(self, item):
        self.linked_list.remove(item)
        self.linked_list.push_head(item)
        
    def evict(self):
        last_item = self.linked_list.pop_tail()
        self.items.pop(last_item.key)
        
 # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#time complexity of all operations is O(1)
#Explanation: All operations on a hash table take constant time.
#Operations at the head and tail of a doubly linked list take constant
#time if you use a tail pointer. Lastly, storing the nodes in a hash table
#allows you to perform the deletion from the linked list in constant time as well.

#overall space complexity: O(n), where "n" is the number of items in the cache

#Explanation: This solution is very space heavy as it uses a hash table(dictionary)
#combined with a doubly linked list O(2n). However, this  
#is necessary in order to achieve constant time operations for all 
# of the methods

        