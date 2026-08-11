# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        list1 = l1
        list2 = l2
        
        while (list1 != None):
            n1 += (str(list1.val))
            list1 = list1.next
        
        while (list2 != None):
            n2 += (str(list2.val))
            list2 = list2.next
    

        reversed_n1 = n1[::-1]
        reversed_n2 = n2[::-1]

        uno = int(reversed_n1)
        dos = int(reversed_n2)

        result = uno + dos

        str_result = str(result)

        str_result = str_result[::-1]

        index = len(str_result)

        head = ListNode(int(str_result[0]))

        curr = head

        for char in str_result[1:]:
            new_node = ListNode(int(char))

            curr.next = new_node

            curr = new_node

        return head

        





