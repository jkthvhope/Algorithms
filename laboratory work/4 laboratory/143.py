from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        previous = None
        current = second
        while current:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp

        first = head
        second = previous

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

list_items = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Список до перемешивания:")
temp = list_items
while temp:
    print(temp.val, end=" -> " if temp.next else "\n")
    temp = temp.next

sol = Solution()
sol.reorderList(list_items)

print("Результат перемешивания:")
res = list_items
while res:
    print(res.val, end=" -> " if res.next else "\n")
    res = res.next