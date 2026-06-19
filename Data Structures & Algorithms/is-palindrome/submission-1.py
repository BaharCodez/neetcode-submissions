class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        s = ''.join(filter(str.isalnum, s))
        length = len(s)
        j = length - 1
        print(s)
        while j > i :
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
        

        