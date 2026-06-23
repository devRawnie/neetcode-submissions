# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        half = math.ceil(n / 2)
        n1 = head
        prev = None
        n2 = head
        for i in range(half):
            prev = n2
            n2 = n2.next

        prev.next = None

        prev = None        
        h2 = n2
        while h2:
            temp = h2.next
            h2.next = prev
            prev = h2
            h2 = temp

        p1 = n1
        p2 = prev

        # k1 = p1
        # while k1:
        #     print(k1.val, end="=>")
        #     k1 = k1.next

        # print()
        # k1 = p2
        # while k1:
        #     print(k1.val, end="=>")
        #     k1 = k1.next

        while p1 and p2:
            t1 = p1.next
            t2 = p2.next
            p1.next = p2
            p2.next = t1
        
            p1 = t1
            p2 = t2




                

