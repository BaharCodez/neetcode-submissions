class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        
        # Loop through s2 up to the point where a full window of 'size' can fit
        for r in range(len(s2) - size + 1):
            # Grab the chunk of s2 with the same length as s1
            substring = s2[r : r + size]
            
            # If the sorted chunk matches the sorted s1, you found a permutation!
            if sorted(substring) == sorted(s1):
                return True
                
        return False