# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        ans = None
        if l1.val <= l2.val:
            ans = l1
            ans.next = self.mergeTwoLists(l1.next, l2)
        else:
            ans = l2
            ans.next = self.mergeTwoLists(l1, l2.next)
        return ans
