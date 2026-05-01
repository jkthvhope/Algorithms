from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            new_node = ListNode(total % 10)

            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head


list1 = ListNode(2, ListNode(4, ListNode(3)))
list2 = ListNode(5, ListNode(6, ListNode(4)))

print("Первое число (развернуто):")
t1 = list1
while t1:
    print(t1.val, end=" -> " if t1.next else "\n")
    t1 = t1.next

print("Второе число (развернуто):")
t2 = list2
while t2:
    print(t2.val, end=" -> " if t2.next else "\n")
    t2 = t2.next

sol = Solution()
res = sol.addTwoNumbers(list1, list2)

print("Результат сложения:")
while res:
    print(res.val, end=" -> " if res.next else "\n")
    res = res.next