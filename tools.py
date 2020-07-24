class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        if self.next:
            return "{}".format(self.val) + " -> " + self.next.__repr__()
        else:
            return "{}".format(self.val)


def array_to_list(ls):
    point = head = ListNode(-1)
    for node in ls:
        point.next = ListNode(node)
        point = point.next

    return head.next
