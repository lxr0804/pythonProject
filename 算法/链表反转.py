class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head

        temp = head.next
        newHead = self.reverse(head.next)
        temp.next = head
        head.next = None

        return newHead

s = Solution()

head = LinkNode(1)
head.next = LinkNode(2)
head.next.next = LinkNode(3)
head.next.next.next = LinkNode(4)

newHead = s.reverse(head)

while (newHead is not None):
    print newHead.val
    newHead = newHead.next
