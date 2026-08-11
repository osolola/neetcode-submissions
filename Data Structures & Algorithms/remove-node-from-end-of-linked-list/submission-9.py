# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next

        index = count - n
        
        if index == 0:
            return head.next
            
        real_curr = head
        current_index = 0
        while real_curr != None and current_index < index - 1:
            real_curr = real_curr.next
            current_index += 1

        deleted_node = real_curr.next
        next_node = deleted_node.next

        real_curr.next = next_node

        return head



            