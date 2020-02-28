"""This is my solution to Leetcode problem 146: LRU Cache."""

class CacheItem:
    """Class to represent an item in a cache."""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """Class to represent a LRU Cache."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = {}
        self.total_items = 0

        #dummy pointers to avoid NoneType exception when removing nodes
        self.head = CacheItem(None, None)
        self.tail = CacheItem(None, None)

        #wire the head and the tail together
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """Given a key, return an item from the cache.
        Return -1 if the item is not in the cache.
        """
        #return none if the item isn't in the cache
        if key not in self.items:
            return -1

        #retrieve the item from the dictionary
        item = self.items[key]

        #move it to the front of the list since it is the
        #most recently accessed item
        self.move_to_head(item)
        return item.value

    def put(self, key: int, value: int) -> None:
        """Given a key and a value, add an item to the cache.
        If the cache is full, the least recently used item
        will be evicted.
        """
        #first check if item in already in the cache
        item = self.items.get(key, None)

        #if not create a new item
        if item is None:
            #if the cache is full, evict the last item
            if self.is_full():
                self.evict()
            item = CacheItem(key, value)

            #add it to the dictionary
            self.items[key] = item

            #insert it at the front on the linked list
            self.push_front(item)

            #increment number of items by 1
            self.total_items += 1
        else:
            #update the value of the found item
            #move it to the front of the list since it is now
            #the most recently accessed item
            item.value = value
            self.move_to_head(item)

    def push_front(self, item):
        """Insert the given item to the front of the linked list."""
        #point the item's previous pointer to head and its
        #next pointer to the item after the head
        item.prev = self.head
        item.next = self.head.next

        #the item is still not fully in the linked list yet
        #point the item after the head's previous pointer to
        #the new item and point the head's next pointer to the item

        self.head.next.prev = item
        self.head.next = item

    def pop_tail(self):
        """Remove the item that is at the end of the linked list."""
        #get item before the tail pointer
        previous_item = self.tail.prev

        #call to method to remove from linked list
        self.remove_from_list(previous_item)
        return previous_item

    def move_to_head(self, item):
        """Remove the item from where it is in the list and 
        move it to the head of the list."""
        #call to method to remove item from the linked list
        self.remove_from_list(item)

        #insert item at the head of the list
        self.push_front(item)

    def remove_from_list(self, item):
        """Remove the given item from the linked list."""
        #get previous an next items in the list
        previous_item = item.prev
        next_item = item.next

        #change their pointers to point towards one another
        previous_item.next = next_item
        next_item.prev = previous_item

    def evict(self):
        """Remove the last item in the linked list and delete it from
        the self.items dictionary."""
        #call to method to remove the last item
        tail = self.pop_tail()

        #delete item from self.items dictionary
        self.items.pop(tail.key)

        #reduce number of items in the cache by 1
        self.total_items -= 1

    def is_full(self):
        """Return True if the cache has reached max capacity."""
        return self.total_items == self.capacity


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

        