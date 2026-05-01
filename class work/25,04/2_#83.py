from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


if __name__ == "__main__":
    node5 = ListNode(3)
    node4 = ListNode(3, node5)
    node3 = ListNode(2, node4)
    node2 = ListNode(1, node3)
    node1 = ListNode(1, node2)

    print([1,1,2,3,3])
    solver = Solution()
    new_head = solver.deleteDuplicates(node1)

    curr = new_head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next