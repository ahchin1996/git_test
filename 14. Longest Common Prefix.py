class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0:
            return prefix
        first = strs[0]
        prefix_test = ""
        situation = True

        for j in range(len(first)):
            prefix_test = prefix_test + first[j]

            for i in strs:
                if i.startswith(prefix_test) == False:
                    situation = False
                    break

            if  situation == False:
                break
            prefix = prefix + prefix_test[j]

        return prefix

        #zip 的用法、set 的方法
        # prefix = ""
        # for i in zip(*strs):
        #     if len(set(i)) > 1:
        #         break
        #     else:
        #         prefix = prefix + i[0]
        # return prefix
def main():
    A = Solution()
    s =  [""]
    ans = A.longestCommonPrefix(s)
    print(ans)

main()

