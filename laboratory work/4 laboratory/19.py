from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for step in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

list_items = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2

print("Исходный список:")
t = list_items
while t:
    print(t.val, end=" -> " if t.next else "\n")
    t = t.next

sol = Solution()
res = sol.removeNthFromEnd(list_items, n)

print(f"Результат (удален {n}-й с конца):")
while res:
    print(res.val, end=" -> " if res.next else "\n")
    res = res.next