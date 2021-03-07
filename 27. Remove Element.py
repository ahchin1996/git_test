class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # n = len(nums)
        # i = 0
        # for j in range(0, n):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        # return i
        n = nums.count(val)
        for i in range(0,n):
            nums.remove(val)
        return len(nums)

def main():
    A = Solution()
    nums =  [3,2,2,3]
    val = 3
    i = A.removeElement(nums,val)
    print(f"{i} , nus = {nums}")


main()
