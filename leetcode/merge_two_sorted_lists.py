# Given the head nodes of two sorted linked lists, list1 and list2
# Merge the two lists into one sorted linked list
# return the head node of the new sorted list
# Edge case: either or both lists could be empty
# Edge case: lists could be different lengths

# Definition for singly-linked list.
from types import new_class


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
    # init pointers for current nodes in l1 and l2
    curl1 = list1
    curl2 = list2
    # init merged list head to return as None
    new_head = ListNode('dummy')
    # init pointer for merged list as dummy node
    merged_cur = ListNode()

    # while loop if there are curs in l1 and l2
    while curl1 and curl2:
        if curl1.val <= curl2.val:
            if new_head.val == 'dummy':
                # set merged list head to l1
                new_head = ListNode()
                new_head.next = curl1
            # set merged list cur.next to l1
            merged_cur.next = curl1
            # set merged list cur to l1
            merged_cur = curl1
            # move cur1 pointer to cur1.next
            curl1 = curl1.next

        # else curl2.val is less than curl1.val
        else:
            if new_head.val == 'dummy':
                # set merge list head to curl2
                new_head = ListNode()
                new_head.next = curl2
            # set merged list cur.next to l2
            merged_cur.next = curl2
            # set merged list cur to l2
            merged_cur = curl2
            # move cur2 to cur2.next
            curl2 = curl2.next
    # Now either both lists are the same length and new_head.next can be returned
    # or we need conditionals if lists were different lengths to just loop through them and add to the merged list
    if curl1:
        # while loop through rest of list 2
        while curl1:
            if new_head.val == 'dummy':
                # set merged list head to l1
                new_head = ListNode()
                new_head.next = curl1
            # tack curl1 onto merged list
            merged_cur.next = curl1
            merged_cur = curl1
            curl1 = curl1.next
    if curl2:
        # while loop through rest of list 2
        while curl2:
            if new_head.val == 'dummy':
                # set merged list head to l2
                new_head = ListNode()
                new_head.next = curl2
            # tack curl2 onto merged list
            merged_cur.next = curl2
            merged_cur = curl2
            curl2 = curl2.next

    return new_head.next

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

print_list(merge_two_lists(l11, l21)) # [1,1,2,3,4,4]
print_list(merge_two_lists(None, None)) # []
print_list(merge_two_lists(None, l23)) # [4]
