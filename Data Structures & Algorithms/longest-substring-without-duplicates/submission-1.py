class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        setstr=set()
        for r in range (len(s)):
            while s[r] in setstr:
                setstr.remove(s[l])
                l=l+1
            setstr.add(s[r])
            res=max(res,r-l+1)
        return res