class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        all = 0
        original = x
        if x < 0 :
            return  False
        else:
            while x != 0:
                Digits = x % 10
                all = (all + Digits)*10
                x = x  // 10

            all = all // 10

            if all < 2 ** 31 and all > -2 ** 31:
                all = all
            else:
                all = 0

            if all == original:
                return True
            else:
                return False

def main():
    A = Solution()
    x = 123
    ans = A.isPalindrome(x)
    print(ans)

main()