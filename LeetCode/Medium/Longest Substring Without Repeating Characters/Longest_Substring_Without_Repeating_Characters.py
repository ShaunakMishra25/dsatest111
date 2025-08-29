class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlen = 0
        start = 0

        seen = {}

        for i, c in enumerate(s):

            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                maxlen = max(maxlen, i-start+1)

            seen[c] = i

        return maxlen