class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for i in range(len(strs)):
            strs[i] == sorted(strs[i])
            print(strs)
        strs.sort()
        i=0
        j =0
        while j< len(strs)-1:
            if strs[i] == strs[j]:
                j +=1
        