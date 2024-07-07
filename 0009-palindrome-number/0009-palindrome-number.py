class Solution:
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)
        strnumrev = "".join(reversed(strnum))
        if (strnum == strnumrev):
            return True
        return False