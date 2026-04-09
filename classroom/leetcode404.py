class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        total = 0

        # check if left child is a leaf
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        # recurse
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total
