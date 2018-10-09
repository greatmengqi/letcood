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

        ans = end = None
        flag = 0

        while l1 and l2:
            temp = ListNode(0)
            temp.val = (l1.val + l2.val + flag) % 10
            flag = (l1.val + l2.val + flag) // 10

            if end is None:
                ans = end = temp
            else:
                end.next = temp
                end = end.next

            l1 = l1.next
            l2 = l2.next

        while flag:
            if l1:
                l1.val = (l1.val + flag) % 10
                flag = (l1.val + flag) // 10
                end.next = l1
                l1 = l1.next
            if l2:
                l2.val = (l2.val + flag) % 10
                flag = (l2.val + flag) // 10
                end.next = l2
                l2 = l2.next

        if l1:
            end.next = l1
        if l2:
            end.next = l2

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


l1 = listToListNode([2, 3, 4])
l2 = listToListNode([7, 8, 9, 10])

s = Solution()
s.addTwoNumbers(l1, l2)
