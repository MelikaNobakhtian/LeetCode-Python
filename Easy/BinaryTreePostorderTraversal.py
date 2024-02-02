# LeetCode 145: Binary Tree Postorder Traversal
# Problem link: https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visited = [False]

        while stack:
            print(stack)
            curr, visit = stack.pop(), visited.pop()
            if curr:
                if visit:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)

        return res
                
        