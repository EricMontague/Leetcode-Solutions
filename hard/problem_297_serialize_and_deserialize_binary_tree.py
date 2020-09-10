"""This is my solution for Leetcode problem 297: Serialize and Deserialize Binary Tree."""

# time complexity: O(n), where 'n' is the number of nodes in the binary tree
# space complexity: O(n), where 'n' is the number of nodes in the binary tree

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return [None]
        serializedTree = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is None:
                serializedTree.append(node)
            else:
                serializedTree.append(node.val)
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
        self.pruneNullLeafNodePointers(serializedTree)
        return serializedTree
    
    def pruneNullLeafNodePointers(self, serializedTree):
        while serializedTree and serializedTree[-1] is None:
            serializedTree.pop()
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serializedTreeDeque = deque(data)
        deserializedTreeDeque = deque()
        rootValue = serializedTreeDeque.popleft()
        if rootValue is None:
            return rootValue
        root = TreeNode(rootValue)
        deserializedTreeDeque.append(root)
        while serializedTreeDeque:
            node = deserializedTreeDeque.popleft()
            leftChildValue = serializedTreeDeque.popleft()
            if serializedTreeDeque:
                rightChildValue = serializedTreeDeque.popleft()
            else:
                rightChildValue = None
            if leftChildValue is not None:
                node.left = TreeNode(leftChildValue)
                deserializedTreeDeque.append(node.left)
            if rightChildValue is not None:
                node.right = TreeNode(rightChildValue)
                deserializedTreeDeque.append(node.right)
        return root


 # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))