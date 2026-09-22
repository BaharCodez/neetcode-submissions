class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l= 0
        r= l+1
        count = {}
        val = k
        for r, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
             #what to return if the key doesn't exist.
            if (( r-l+1 )-max(count.values())) > k:
                count[s[l]] -= 1
                l +=1

            val = max(r-l+1, val)
            
        return val
            # loop: changing length of window based on if theres more than k replacements needed to maintain
            # keep track of letter with most frequency and make sure other is <k using hashtable
            # brute force solution: try every combination
            # efficient sol: sliding window

            
        

        