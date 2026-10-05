class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset=set(s)
        res=0
        for i in charset:
            count=l=0
            for j in range(len(s)):
                if s[j]==i:
                    count=count+1
                while(j-l+1)-count>k:
                    if s[l]==i:
                        count=count-1
                    l=l+1
                res=max(res,j-l+1)
        return res