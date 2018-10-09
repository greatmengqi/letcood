# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        ans = l1
        flag = 0

        while l1.next and l2.next:
            temp = (l1.val + l2.val + flag) % 10
            flag = (l1.val + l2.val + flag) // 10
            l1.val = temp
            l1 = l1.next
            l2 = l2.next
        else:
            temp = (l1.val + l2.val + flag) % 10
            flag = (l1.val + l2.val + flag) // 10
            l1.val = temp

        while flag:
            if l1.next:
                l1 = l1.next
                temp = (l1.val + flag) % 10
                flag = (l1.val + flag) // 10
                l1.val = temp
            elif (l2.next is None):
                l1.next = ListNode(flag)
                flag = 0
            if l2.next:
                l1.next = l2.next
                l2.next = None
        if l1.next:
            pass
        if l2.next:
            l1.next = l2.next
        return ans


def listToListNode(l):
    ans = end = None
    for i in l:
        temp = ListNode(i)
        if end is None:
            ans = end = temp
        else:
            end.next = temp
            end = end.next
    return ans


l1 = listToListNode([1])
l2 = listToListNode([9,9])

s = Solution()
s.addTwoNumbers(l1, l2)
