# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        h1 = list1
        h2 = list2
        while h1 and h2:
            if h1.val < h2.val:
                temp.next = ListNode(h1.val)
                temp = temp.next
                h1 = h1.next

            else:
                temp.next = ListNode(h2.val)
                temp = temp.next
                h2 = h2.next

        while h1:
            temp.next = ListNode(h1.val)
            temp = temp.next
            h1 = h1.next

        while h2:
            temp.next = ListNode(h2.val)
            temp = temp.next
            h2 = h2.next

        return head.next
