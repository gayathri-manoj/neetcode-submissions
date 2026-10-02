class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmax=0
        maxsub=nums[0]
        for i in nums:
            if curmax<0:
                curmax=0
            curmax+=i
            maxsub=max(maxsub,curmax)
        return maxsub