class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums)==k:
            return float(sum(nums) / float(k))
        winsum=sum(nums[:k])
        maxsum=winsum
        for i in range(k,len(nums)):
            winsum+=nums[i]-nums[i-k]
            maxsum=max(maxsum,winsum)
        res=float(maxsum)/k
        return res