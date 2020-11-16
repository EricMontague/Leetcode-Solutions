"""This file contains my solutions to Leetcode problm 337: House Robber III."""


# time complexity: O(n), where 'n' is the number of nodes in the binary tree
# space complexity: O(n)

# Need two memo tables because each node gets called twice, once with the
# value of True and once with the value of False for parent_robbed
# There are two types of calls made to rob_houses()
# One returns the max amount you can make if you choose to rob the house,
# the other returns the max amount you can make if you choose to pass on the house
# which changes how you determine the return value for the function
class Solution:
    def rob(self, root: TreeNode) -> int:
        memo_robbed = {}
        memo_not_robbed = {}
        
        def rob_houses(node, parent_robbed):
            if node is None:
                return 0
            # Find out he max amount if you rob this house
            if not parent_robbed:
                if node in memo_robbed:
                    return memo_robbed[node]
                max_if_rob = (
                    node.val
                    + rob_houses(node.left, True)
                    + rob_houses(node.right, True)
                )
                max_if_not_rob = (
                    rob_houses(node.left, False)
                    + rob_houses(node.right, False)
                )
                memo_robbed[node] = max(max_if_rob, max_if_not_rob)
                return memo_robbed[node]
            # Find out the max amount if you pass on this house
            else:
                if node in memo_not_robbed:
                    return memo_not_robbed[node]
                max_if_not_rob = (
                    rob_houses(node.left, False)
                    + rob_houses(node.right, False)
                )

                memo_not_robbed[node] = max_if_not_rob
                return max_if_not_rob
        
        return rob_houses(root, False)
        
    
    

# time complexity: O(n), where 'n' is the number of nodes in the binary tree
# space complexity: O(h), where 'h' is the height of the binary tree
# Explanation - https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.rob_houses(root))
    
    def rob_houses(self, node):
        if node is None:
            return (0, 0)
        left = self.rob_houses(node.left)
        right = self.rob_houses(node.right)
        
        # if we rob this node, we cannot rob its children
        rob = node.val + left[1] + right[1]
        
        # else we could choose to either rob its children or not
        not_rob = max(left) + max(right)
        return (rob, not_rob)
