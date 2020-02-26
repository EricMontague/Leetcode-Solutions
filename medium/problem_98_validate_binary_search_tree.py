# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        last_seen = float("-inf")

        #initialize stack to hold nodes
        stack = []
        while stack or root:
            #traverse left subtree
            #go as far left as possible until you hit a null pointer
            while root:
                stack.append(root)
                root = root.left

            #pop node off of the stack and compare it to the 
            #last seen value
            root = stack.pop()
            if last_seen >= root.val:
                return False
            last_seen = root.val

            #you have finished traversing the left subtree,
            #now you need to traverse the right subtree
            root = root.right
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
