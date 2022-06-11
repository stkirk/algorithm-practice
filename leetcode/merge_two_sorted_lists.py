# Given the head nodes of two sorted linked lists, list1 and list2
# Merge the two lists into one sorted linked list
# return the head node of the new sorted list
# Edge case: either or both lists could be empty
# Edge case: lists could be different lengths

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
    # init pointers for current nodes in l1 and l2
    # init merged list head to return as None
    # init pointer for merged list as None

    # while loop is there are curs in l1 or l2
        # if l1.val <= l2.val:
            # if merged list head is None:
                # set merged list head to l1
            # set merged list cur.next to l1
            # set merged list cur to l1
            # move cur1 pointer to cur1.next

        # else curl2.val is less than curl1.val
            #if merged list head is None:
                # set merge list head to curl2
            # set merged list cur.next to l2
            # set merged list cur to l2
            # move cur1 to cur1.next

    return new_head

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
