# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dum = ListNode(None)
        prev = dum

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1 == None:
            prev.next = l2
        elif l2 == None:
            prev.next = l1

        return dum.next

def main():
    A = Solution()
    l1 = None
    l2 = ListNode(0)
    # l1 = ListNode(1)
    # l1.next = l1_2 = ListNode(2)
    # l1_2.next = ListNode(4)
    # l2 = ListNode(1)
    # l2.next = l2_2 = ListNode(3)
    # l2_2.next = ListNode(4)
    ans = A.mergeTwoLists(l1,l2)
    while ans:
        print(ans.val)
        ans = ans.next

main()

