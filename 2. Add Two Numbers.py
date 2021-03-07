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
        if len(l1) == 0 or len(l1) > 100:
            result = 0
            return result
        if len(l2) == 0 or len(l2) > 100:
            result = 0
            return result

        result = 1
        return  result



def main():
    A = Solution()
    l1 = [2,4,3]
    l2 = [5, 6, 4]
    z = A.addTwoNumbers(l1,l2)
    print(z)

main()


l1 = [2,4,3]
l2 = [5,6,4,8]
l1_len = len(l1)
l2_len = len(l2)

# if l1_len == l2_len
#     result = []
#     for i in range(len(l1)):
#         ans =  l1[i] + l2[i]
#         if ans <0 or ans >9:
#             ans = 0
#         result.append( l1[i] + l2[i])
#     return result
# else:
#
