from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp
        return previous

node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

temp = node1
while temp:
    print(temp.val, end=" -> " if temp.next else "\n")
    temp = temp.next

sol = Solution()
res = sol.reverseList(node1)

while res:
    print(res.val, end=" -> " if res.next else "")
    res = res.next