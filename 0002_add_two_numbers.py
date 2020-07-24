# Definition for singly-linked list.
"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

from tools import *


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = []
        flag = 0
        while l1 and l2:
            temp = flag + l1.val + l2.val
            flag = temp // 10
            temp = temp % 10
            ans.append(temp)
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp = flag + l1.val
            flag = temp // 10
            temp = temp % 10
            ans.append(temp)
            l1 = l1.next

        while l2:
            temp = flag + l2.val
            flag = temp // 10
            temp = temp % 10
            ans.append(temp)
            l2 = l2.next

        if flag:
            ans.append(flag)

        point = head = ListNode(-1)
        for i in ans:
            point.next = ListNode(i)
            point = point.next
        return head.next


print(Solution().addTwoNumbers(array_to_list([2, 4, 3]), array_to_list([5, 6, 4])))
