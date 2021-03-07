class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = len(nums)-1
        if len(nums) == 0:
            return 0
        i=1
        while i <= len_:
            if nums[i] == nums[i-1]:
                del nums[i]
                len_ -=1
            else:
                i+=1
                continue
        return nums

def main():
    A = Solution()
    arr =  [1,1,2]
    ans = A.removeDuplicates(arr)
    print(len(ans),", nums = ",ans)

main()

