class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #want to have a longest pref variable
        # look at the start of each word in the array and if they are all equal then add that.
        # compare the first value with every other strong in coming getting small and smaller when tit doesdnt match to bat compares with bag only have ba so next word does bank have ba yas next band have ba yas

        stri = strs[0]
        for s in strs:
            i =0
            while i <len(s) and i <len(stri) and s[i] == stri[i] :
                i +=1
            
            stri = s[:i]

        return stri
        
        