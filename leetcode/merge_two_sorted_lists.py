# Given the head nodes of two sorted linked lists, list1 and list2
# Merge the two lists into one sorted linked list
# return the head node of the new sorted list
# Edge case: either or both lists could be empty

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# helper to print linked list given a node
def print_list(node):
    cur = node
    node_list = []
    while cur:
        node_list.append(cur.val)
        cur = cur.next
    print(node_list)

def merge_two_lists(list1, list2):

    return list1

# test case linked list nodes
l11 = ListNode(1)
l12 = ListNode(2)
l11.next = l12
l13 = ListNode(4)
l12.next = l13

l21 = ListNode(1)
l22 = ListNode(3)
l21.next = l22
l23 = ListNode(4)
l22.next = l23

print_list(merge_two_lists(l11, l21))
