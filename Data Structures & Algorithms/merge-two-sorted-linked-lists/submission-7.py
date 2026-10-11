# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        front = res
        
        while list1 and list2:
            if list1.val <= list2.val:
                front.next = list1
                list1 = list1.next
            else:
                front.next = list2
                list2 = list2.next
            front = front.next
        
        if list1:
            front.next = list1
        elif list2:
            front.next = list2
        return res.next
                