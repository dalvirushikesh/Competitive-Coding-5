#Time Complexity = O(n)
#Space Complexity = O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            maxValue = float("-inf")

            for i in range(levelSize):
                node = queue.popleft()
                maxValue = max(maxValue,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(maxValue)
        return result