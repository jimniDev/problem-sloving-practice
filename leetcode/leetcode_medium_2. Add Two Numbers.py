# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1 = reverseLinkedList(l1)
        # l2 = reverseLinkedList(l2)

        r = ListNode()
        cur = r
        head1, head2 = l1, l2
        over = 0
        while head1 or head2:
            sum_val = over
            if head1:
                sum_val += head1.val
                head1 = head1.next
            if head2:
                sum_val += head2.val
                head2 = head2.next
            # print(sum_val)
            if sum_val >= 10:
                over = 1
                sum_val -= 10
            else:
                over = 0

            cur.val = sum_val
            if head1 or head2 or over:
                nxt = ListNode(over)
                cur.next = nxt
                cur = nxt
            else:
                cur.next = None
            
        return r


# def reverseLinkedList(ll):
#     head = ll
#     tail = None
#     while head:
#         swap = head.next
#         head.next = tail
#         tail = head
#         head = swap # for next step
#     return tail
