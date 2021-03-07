class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n<1 or n>15:
            return False

        s = s.upper()
        d = {"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        all = 0
        i = 0
        try:
            while i < n :
                if d[s[i]] < d[s[i+1]]:
                    all = all + d[s[i+1]] - d[s[i]]
                    i = i + 2
                else:
                    all = all + d[s[i]]
                    i = i + 1
        except IndexError:
            all = all + d[s[i]]

        return all

def main():
    A = Solution()
    s = ""
    ans = A.romanToInt(s)
    print(ans)

main()