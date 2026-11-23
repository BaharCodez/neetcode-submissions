class Solution:
    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s)-1
        changes =0

        def isPali(i, j):
            while i < j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True

        while i <j:
            if s[i] == s[j]:
                i+=1
                j-=1

            else:
                return(isPali( i+1, j) or  isPali(i,j-1))
        
        return True