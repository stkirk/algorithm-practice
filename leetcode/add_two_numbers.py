# given two linked lists with each node representing a digit in an integer
# where the integer is reversed (tail node is first digit, head is last)
# ex (2) -> (4) -> (3) represents the integer 342
# add the two intgers together and return a new reversed linked list representing the sum

# Linked list definition:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    return []

n3 = ListNode(2)
n2 = ListNode(4, n3)
n1 = ListNode(2, n2)
n6 = ListNode(4)
n5 = ListNode(6, n6)
n4 = ListNode(5, n5)
