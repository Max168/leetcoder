# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current,carry = result,0
        while l1 != None or l2 != None:
            res = carry
            if l1 != None:
                res += l1.val
                l1 = l1.next
            if l2 != None:
                res += l2.val
                l2 = l2.next
            carry,res = res // 10,res % 10
            current.next = ListNobe(res)
            current = current.next
        if carry == 1:
            current.next = ListNobe(1)
        return result.next
