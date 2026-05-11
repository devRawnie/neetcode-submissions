# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for li in lists:
            if li:
                heapq.heappush(min_heap, ListNodeWrapper(li))

        dummy_node = ListNode()
        head = dummy_node

        while min_heap:
            n = heapq.heappop(min_heap)
            if n.node.next:
                heapq.heappush(min_heap, ListNodeWrapper(n.node.next))

            head.next = n.node
            head = head.next

        return dummy_node.next

