class Solution(object):
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2
        dummy = ListNode()
        curr = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                curr =  curr.next
                p1 = p1.next
            else: 
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        
        if p1 != None: curr.next = p1
        if p2 != None: curr.next = p2

        return dummy.next