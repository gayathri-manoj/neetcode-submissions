class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin=curmax=1
        maxsub=max(nums)
        for i in nums:
            if i==0:
                curmin=1
                curmax=1
                continue
            temp=curmax *i
            curmax=max(temp,i,i*curmin)
            curmin=min(temp,i*curmin,i)
            maxsub=max(maxsub,curmax)
        return maxsub