class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            x = 0
            y = 0
            for j in range(0, len(nums)):
                if i == j :
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        x = i
                        y = j
                        break
                    else:
                        continue
            if x != 0:
                break
        if x > y:
            x, y = y, x
        return x, y

def main():
    A = Solution()
    nums = [2, 5, 5, 11]
    target = 10
    x , y = A.twoSum(nums,target)
    print(f'Because nums[{x}] + nums[{y}] == {target}, we return [{x},{y}]')

main()