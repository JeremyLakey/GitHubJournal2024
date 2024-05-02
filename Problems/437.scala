/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {

    def triggerTree(node: TreeNode, targetSum: Int): Int = {
        if (node == null) return 0
        return trTree(node, targetSum, 0) + triggerTree(node.right, targetSum) + triggerTree(node.left, targetSum) 
    }

    def trTree(node: TreeNode, targetSum: Int, curr: Int): Int = {
        if (node == null) return 0
        var tot = 0
        if (curr > 0 && node.value > 0 && curr + node.value < 0) return 0
        if (targetSum == curr + node.value) {
            tot += 1
        }

        tot += trTree(node.right, targetSum, curr + node.value)
        tot += trTree(node.left, targetSum, curr + node.value)
        return tot
    }

    def pathSum(root: TreeNode, targetSum: Int): Int = {
        return triggerTree(root, targetSum)
    }
}