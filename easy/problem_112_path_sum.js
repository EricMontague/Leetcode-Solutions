// This file contains my solution to Leetcode problem 122: Path Sum



// time complexity: O(n), where 'n' is the number of nodes in the tree
// space complexity: O(h), where 'h' is the height of the tree

const hasPathSum = function (root, sum) {
    if (root === null) {
        return false;
    }
    const difference = sum - root.val;
    if (difference === 0 && root.left === null && root.right === null) {
        return true;
    }
    return (
        hasPathSum(root.left, difference) || hasPathSum(root.right, difference)
    );
};