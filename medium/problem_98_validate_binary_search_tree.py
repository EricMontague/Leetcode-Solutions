
class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        lastNodeSeen = None
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                node = stack.pop()
                if lastNodeSeen and lastNodeSeen.val >= node.val:
                    return False
                lastNodeSeen = node
                root = node.right
            else:
                return True
  

#Time complexity: O(n) since you visit all of the nodes in the BST at most once

#Space complexity: O(h). For a balanced BST, this will be O(log n), but for
#a skewed BST, this will be O(n), so O(n) would be the worst case if you didn't
#know if the BST would be balanced or not

#Approach: The problem can be solved using an iterative inorder traversal
#that also keeps track of the value of the last node that was seen. In order
#for the binary tree to be a valid BST, an inorder traversal of the nodes would
#print them out in sorted order. By checking the value of the previous seen
#node as you go, you can see whether the values are progressing in sorted
#order or not.
