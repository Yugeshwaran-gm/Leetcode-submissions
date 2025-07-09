class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count={}
        count[0]=1
        odd=0
        res=0
        for n in nums:
            if n%2!=0:
                odd+=1
            res+=count.get(odd-k,0)
            count[odd]=count.get(odd,0)+1
        return res