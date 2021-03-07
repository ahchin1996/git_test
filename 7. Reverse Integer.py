class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 0
        if x <0:
            x = x*-1
            negative = 1
        all = 0
        while x != 0:
            digit = x % 10
            x = x // 10
            all = (all + digit)*10

        all = all // 10

        if negative == 1:
            all =  all *-1

        if all < 2 ** 31 and all > -2 ** 31:
            all = all
        else:
            all = 0

        return all

def main():
    A = Solution()
    x = 1534236469
    z = A.reverse(x)
    print(z)

main()

