class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def empty(self) -> bool:
        return not self.s1 and not self.s2

print("Вход:")
print('["MyQueue", "push", "push", "peek", "pop", "empty"]')
print('[[], [1], [2], [], [], []]')

myQueue = MyQueue()
results = [None]

myQueue.push(1)
results.append(None)

myQueue.push(2)
results.append(None)

results.append(myQueue.peek())

results.append(myQueue.pop())

results.append(myQueue.empty())

print("\nВыход:")
formatted_results = [str(r).lower() if r is not None else "null" for r in results]
print("[" + ", ".join(formatted_results) + "]")