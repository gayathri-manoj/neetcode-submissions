class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dynamic programming 
        '''cursum=0
        maxsub=nums[0]
        for i in nums:
            if cursum<0:
                cursum=0
            cursum+=i
            maxsub=max(maxsub,cursum)
        return maxsub'''

        #bruteforce
        '''res = nums[0]
        for i in range(len(nums)):
            cur = 0
            for j in range(i,len(nums)):
                cur += nums[j]
                res = max(res, cur)
        return res'''

        #or dynamic prgm method
        s=nums[0]
        maxsum=s
        for n in nums[1:]:
            s= max(n,s+n)
            maxsum=max(maxsum,s)
        return maxsum