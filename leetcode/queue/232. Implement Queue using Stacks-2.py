# stack 으로 queue 만들기
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        new_stack = [x]
        for i in self.stack:
            new_stack.append(i)

        self.stack = new_stack

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
