from src.challenges import (
    ActionStack,
    RequestQueue,
    is_note_balanced,
    process_request_line,
)


def test_action_stack_push_pop_peek() -> None:
    stack = ActionStack()
    stack.push("open ticket")
    stack.push("assign worker")
    assert stack.peek() == "assign worker"
    assert stack.pop() == "assign worker"
    assert stack.pop() == "open ticket"


def test_action_stack_empty_cases() -> None:
    stack = ActionStack()
    assert stack.is_empty() is True
    assert stack.pop() is None
    assert stack.peek() is None


def test_request_queue_enqueue_dequeue_peek() -> None:
    queue = RequestQueue()
    queue.enqueue("Mina")
    queue.enqueue("Jay")
    assert queue.peek() == "Mina"
    assert queue.dequeue() == "Mina"
    assert queue.dequeue() == "Jay"


def test_request_queue_empty_cases() -> None:
    queue = RequestQueue()
    assert queue.is_empty() is True
    assert queue.dequeue() is None
    assert queue.peek() is None


def test_is_note_balanced_true_cases() -> None:
    assert is_note_balanced("Call back (urgent)") is True
    assert is_note_balanced("Repair request [building A]") is True
    assert is_note_balanced("Issue details: {network}[floor 2]") is True
    assert is_note_balanced("") is True


def test_is_note_balanced_false_cases() -> None:
    assert is_note_balanced("(]") is False
    assert is_note_balanced("(()") is False
    assert is_note_balanced("{[}]") is False


def test_process_request_line_normal_case() -> None:
    citizens = ["Mina", "Jay", "Omar"]
    assert process_request_line(citizens) == ["Mina", "Jay", "Omar"]


def test_process_request_line_empty_case() -> None:
    assert process_request_line([]) == []