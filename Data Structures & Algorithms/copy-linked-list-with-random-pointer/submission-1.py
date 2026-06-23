"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodes = {} # orig -> new
        nodes_arr = []
        temp = head
        while temp:
            nn = Node(temp.val)
            nodes_arr.append(nn)
            nodes[temp] = nn
            temp = temp.next

        for k, v in nodes.items():
            print(k.val, v.val)

        new_head = nodes[head]
        temp_new = new_head
        temp = head
        while temp:
            if temp.next:
                temp_new.next = nodes[temp.next]
            if temp.random:
                temp_new.random = nodes[temp.random]
            temp_new = temp_new.next
            temp = temp.next

        return new_head        