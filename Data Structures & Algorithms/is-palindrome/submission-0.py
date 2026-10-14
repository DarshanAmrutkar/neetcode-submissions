class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()]).lower()
        i = len(s)-1
        for char in s[:(len(s)//2)+1]:
            if char == s[i]:
                i-=1
            else:
                return False
        return True
