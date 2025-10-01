class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    if not head.next:
        return head.next
    first = second = head

    i = 0
    while first.next and i < n:
        first = first.next
        i += 1
    if i < n:
        return head.next

    while first.next:
        first = first.next
        second = second.next
    second.next = second.next.next

    return head


def print_LinkedList(root):
    out = []
    node = root
    while node:
        out.append(node.val)
        node = node.next
    print(out)

if __name__ == '__main__':
    h = [1,2]
    hd = ListNode(h[0])
    node = hd
    for i in range(2, len(h) + 1):
        node.next = ListNode(i)
        node = node.next

    result = removeNthFromEnd(hd, 1)
    print_LinkedList(result)



