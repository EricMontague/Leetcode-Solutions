"""This is my solution for Leetcode problem 297: Serialize and Deserialize Binary Tree."""

# time complexity: O(n), where 'n' is the number of nodes in the binary tree
# space complexity: O(n), where 'n' is the number of nodes in the binary tree

from collections import deque

from collections import deque


class Codec:
    
    SERIALIZED_NULL_POINTER = "#"
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        serializedTree = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
                serializedTree.append(str(node.val))        
            else:
                serializedTree.append(self.SERIALIZED_NULL_POINTER)
        self.pruneNullLeafNodePointers(serializedTree)
        return ",".join(serializedTree)
    
    def pruneNullLeafNodePointers(self, serializedTree):
        while serializedTree[-1] == self.SERIALIZED_NULL_POINTER:
            serializedTree.pop()
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        childNodeQueue = self.buildDeserializedNodeQueue(data)
        root = childNodeQueue.popleft()
        parentNodeQueue = deque([root])       
        while childNodeQueue:
            parentNode = parentNodeQueue.popleft()
            leftChild = childNodeQueue.popleft()
            if leftChild:
                parentNode.left = leftChild
                parentNodeQueue.append(parentNode.left)
            if childNodeQueue:
                rightChild = childNodeQueue.popleft()
                if rightChild:
                    parentNode.right = rightChild
                    parentNodeQueue.append(parentNode.right)       
        return root
    
    def buildDeserializedNodeQueue(self, data):
        nodes = deque()
        for value in data.split(","):
            if value != self.SERIALIZED_NULL_POINTER:
                nodes.append(TreeNode(int(value)))
            else:
                nodes.append(None)
        return nodes