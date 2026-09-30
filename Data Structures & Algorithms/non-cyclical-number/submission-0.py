class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while(n!=1 and n not in s):
            s.add(n)
            res=0
            while(n):
                res+=(n%10)**2
                n=n//10
            n=res
        if n==1:
            return True
        else:
            return False 