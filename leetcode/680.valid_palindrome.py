class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        length=len(s)
        x=''
        for i in range(length):
            if not i == length or s[i] == s[(length-i)-1]:
                if i == 0 and not s[i] == s[(length-i)-1]:
                    return False
                continue
            else:
                if s[i] == s[i+1]:
                    x=s.remove([i+2])
                else:
                    x=s.remove([i+1])
                    print(x)
        if x == x[::-1]:
            return True
        return False
a=Solution()
print(a.validPalindrome("abca"))
