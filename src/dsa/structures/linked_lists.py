from dataclasses import dataclass
from typing import *

DataType = Union[str | int | float | bytes]


@dataclass
class ListNode:
    val: Optional[DataType] = None
    next: Optional[DataType] = None

    def __eq__(self, other):
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
        return node
    recurse_traverse(node.next)
    print(node.val, end="")

def recurse_traverse_reverse(node: Optional[ListNode]):
    """ O(N), O(N)
    space complexity is due to call stack being size n"""
    if node is None or node.next is None:
        return node
    thing = recurse_traverse_reverse(node.next)
    node.next.next = node
    node.next = None
    return thing


if __name__ == "__main__":
    s: ListNode = tree_from_iterable(range(10))
    print(recurse_traverse_reverse(s))

    s = tree_from_iterable("hello, stuff")
    recurse_traverse(s)
