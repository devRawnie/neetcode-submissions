# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow and fast:
            if slow:
                slow = slow.next
            else:
                break

            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            else:
                break

            if slow == fast:
                break

        if slow and fast and slow == fast:
            return True

        return False