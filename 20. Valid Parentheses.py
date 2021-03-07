class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s)> 0 :
            if "()" in s or "[]" in s or "{}" in s:
                s = s.replace("()","")
                s = s.replace("[]","")
                s = s.replace("{}","")
            else:
                break
        if len(s) >0:
            return False
        else:
            return True

def main():
    A = Solution()
    s = "([)]"
    ans = A.isValid(s)
    print(ans)

main()