from dataclasses import dataclass
from typing import *

DataType = Union[str | int | float | bytes]


@dataclass
class ListNode:
    val: Optional[DataType] = None
    next: Optional[DataType] = None

    def __eq__(self, other):
        if other is None:
            return False
        return isinstance(self.val, type(other.val)) and self.val == other.val


def tree_from_iterable(i: Iterable) -> ListNode:
    """list in, tree out"""
    prehead = node_iter = ListNode()
    for val in i:
        node_iter.next = ListNode(val)
        node_iter = node_iter.next
    return prehead.next

def recurse_traverse(node: Optional[ListNode]):
    if node is None:
        return
    recurse_traverse(node.next)
    print(node.val, end=" ")

def recurse_traverse_reverse(node: Optional[ListNode]):
    """ O(N), O(N)
    space complexity is due to call stack being size n"""
    if node is None or node.next is None:
        return node
    thing = recurse_traverse_reverse(node.next)
    node.next.next = node
    node.next = None
    return thing

def stack_traverse(node: Optional[ListNode]) -> None:
    """ O(N), O(N)

    really it's O(2N), but remember it's about scaling, so O(2N) reduces to O(N) as constants fall away next to variables
    """
    stack: list[ListNode] = []
    head = node_iter = node
    while node_iter is not None:
        stack.append(node_iter)
        node_iter = node_iter.next
    for i in reversed(range(len(stack))):
        print(stack[i].val, end=" ")
        del stack[i]

def stack_traverse_reverse(node: Optional[ListNode]):
    """ O(N) O(N)

    Uses one traversal, but easily could be two, back and forth.
    one to load up the stack, the other to set all the nexts correctly
    """
    if node == None or node.next == None:
        return node

    stack: list[ListNode] = []
    node_iter = node

    while node_iter is not None:
        stack.append(node_iter)
        node_iter = node_iter.next
        if len(stack) > 1:
            stack[-1].next = stack[-2]
        else:
            stack[0].next = None
    return stack[-1]


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(stack_traverse_reverse(head))
