from __future__ import annotations
from collections import deque


class ActionStack:
    def __init__(self) -> None:
        self.items: list[str] = []

    def push(self, action: str) -> None:
        self.items.append(action)

    def pop(self) -> str | None:
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self) -> str | None:
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


class RequestQueue:
    def __init__(self) -> None:
        self.items: deque[str] = deque()

    def enqueue(self, name: str) -> None:
        self.items.append(name)

    def dequeue(self) -> str | None:
        if self.is_empty():
            return None
        return self.items.popleft()

    def peek(self) -> str | None:
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0


def is_note_balanced(note: str) -> bool:
    stack: list[str] = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in note:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


def process_request_line(citizens: list[str]) -> list[str]:
    queue = deque(citizens)
    result: list[str] = []

    while queue:
        result.append(queue.popleft())

    return result


def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
    stack = actions.copy()

    for _ in range(min(undo_count, len(stack))):
        stack.pop()

    return stack