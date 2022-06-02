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
    # init dummy head
    dummy = ListNode()
    # init cur (return list) to dummy
    cur = dummy
    # init cur_l1 and cur_l2
    cur_l1 = l1
    cur_l2 = l2
    # init carry digit
    carry = 0

    # loop while cur_l1 or cur_l2 or carry
    while cur_l1 or cur_l2 or carry:
        # set values to add with safetly check
        val1 = cur_l1.val if cur_l1 else 0
        val2 = cur_l2.val if cur_l2 else 0
        
        # place_total = cur_l1 + cur_l2 + carry
        place_total = val1 + val2 + carry
        carry = place_total // 10
        place_total = place_total % 10
        # add new node
        cur.next = ListNode(place_total)

        #update pointers
        cur = cur.next
        cur_l1 = cur_l1.next if cur_l1 else None
        cur_l2 = cur_l2.next if cur_l2 else None

        
    return dummy.next

def add_two_numbers_shortcut(l1, l2):
    # init lists for l1 and l2
    list_one = []
    list_two = []
    # loop through l1 and l2 and append values to list
    cur_l1 = l1
    cur_l2 = l2
    while cur_l1:
        list_one.append(cur_l1.val)
        cur_l1 = cur_l1.next
    while cur_l2:
        list_two.append(cur_l2.val)
        cur_l2 = cur_l2.next
    # reverse both list, turn each into integers
    list_one.reverse()
    list_two.reverse()

    # add integers together
    num_1 = int("".join(str(i) for i in list_one))
    num_2 = int("".join(str(i) for i in list_two))
    sum = str(num_1 + num_2)
    # split into new reversed list
    sum_string_list = sum.split()
    sum_int_list = [int(i) for i in sum_string_list]
    sum_int_list.reverse()
    # loop through list creating nodes as you go
    head = None
    cur = None
    for i in sum_int_list:
        if head == None:
            head = ListNode(i)
            cur = head
        else:
            new_node = ListNode(i)
            cur.next = new_node
            cur = cur.next

    return head

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

print_linked_list(add_two_numbers_shortcut(n1, n4))
print_linked_list(add_two_numbers(n1, n4))
