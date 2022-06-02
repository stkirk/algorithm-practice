# given two linked lists with each node representing a digit in an integer
# where the integer is reversed (tail node is first digit, head is last)
# ex (2) -> (4) -> (3) represents the integer 342
# add the two integers together and return a new reversed linked list representing the sum

# Linked list definition:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# pure linked list solution
def add_two_numbers(l1, l2):
    # init cur_l1 and cur_l2
    # init carry digit

    # init sum_list = None
    # cur_sum_list = None

    # loop while cur_l1 or cur_l2
        # safety check if !cur_l1
            # set curl1 to 0
        # safety check if !cur_l2
            # set cur_l2 to 0
        
        # place_total = cur_l1 + cur_l2
        # if place_total > 9:
            # carry_digit = 1
            # place total -= 10

        # if no sum_list
            # sum_list = ListNode(place_total)
            # cur_sum_list = sum_list
        # else:
            # cur_sum_list.next = ListNode(place_total + carry_digit)

        
    return []

def add_two_numbers_shortcut(l1, l2):
    # init lists for l1 and l2
    # loop through l1 and l2 and append values to list
    # reverse both list, turn each into integers
    # add integers together
    # typecase to string
    # split into new reversed list
    # loop through list creating nodes as you go
    # return head

n3 = ListNode(3)
n2 = ListNode(4, n3)
n1 = ListNode(2, n2)
n6 = ListNode(4)
n5 = ListNode(6, n6)
n4 = ListNode(5, n5)

def print_linked_list(node):
    current_node = node
    node_list = []
    while current_node:
        node_list.append(current_node.val)
        current_node = current_node.next
    print(node_list)
