class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        strs = sorted(strs)

        n = len(strs[0])
        if len(strs[0]) > len(strs[-1]):
            n = len(strs[-1])

        for i in range(n):
            if strs[0][i] == strs[-1][i]:
                ans += strs[0][i]
            else:
                break
        return ans


                

         