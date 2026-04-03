class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.k = k  # свободные места

    def enQueue(self, value: int) -> bool:
        if self.k > 0:
            self.queue.append(value)
            self.k -= 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            self.k += 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.k == 0:
            return True
        else:
            return False


print("Вход:")
print('["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]')
print('[[3], [1], [2], [3], [4], [], [], [], [4], []]')

obj = MyCircularQueue(3)
results = [None]

results.append(obj.enQueue(1))
results.append(obj.enQueue(2))
results.append(obj.enQueue(3))

results.append(obj.enQueue(4))

results.append(obj.Rear())
results.append(obj.isFull())

results.append(obj.deQueue())
results.append(obj.enQueue(4))
results.append(obj.Rear())

print("\nВыход:")
formatted = [str(r).lower() if r is not None else "null" for r in results]
print("[" + ", ".join(formatted) + "]")