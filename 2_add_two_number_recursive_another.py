class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if l1.next or l2.next or c:
            l1.next = l1.next if l1.next else ListNode(0)
            l2.next = l2.next if l2.next else ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret