# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []

        # def inorder(root):
        #     if root == None:
        #         return
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)

        # inorder(root)
        # return ans

        st = []
        result = []
        if root is None:
            return []
        curr = root
        while curr != None or len(st) != 0:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                curr = st[-1]
                st.pop()
                result.append(curr.val)
                curr = curr.right
        return result