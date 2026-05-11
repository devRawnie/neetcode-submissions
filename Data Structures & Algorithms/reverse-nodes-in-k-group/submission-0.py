# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next}"

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes_head = []
        temp = 0
        prev = None
        while head:
            if temp % k == 0:
                nodes_head.append([head, True])
                if prev:
                    prev.next = None

            prev = head
            head = head.next
            temp += 1

        if temp % k != 0:
            nodes_head[-1][-1] = False

        def reverse(n):
            p = None
            dummy = n
            while dummy:
                temp = dummy.next
                dummy.next = p
                p = dummy
                dummy = temp

            return p

        reversed_nodes = []
        for node in nodes_head:
            new_head = reverse(node[0]) if node[1] else node[0]
            reversed_nodes.append(new_head)

        dummy = ListNode()
        head = dummy
        for node in reversed_nodes:
            dummy.next = node
            temp = node
            while temp.next:
                temp = temp.next

            dummy = temp

        return head.next



