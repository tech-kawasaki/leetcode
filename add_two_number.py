# Definition for singly-linked list.
from typing import Optional

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.recursive(l1, l2, 0,ListNode(0))

    def recursive(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int, tail: ListNode) -> tuple(ListNode, int):
        if not(l1 or l2):
            return None
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)

        carry, out = divmod(val1 + val2 + carry, 10)
        tail.next = ListNode(out)

        self.recursive((l1.next if l1 else None), (l2.next if l2 else None), carry, tail.next)
        return tail