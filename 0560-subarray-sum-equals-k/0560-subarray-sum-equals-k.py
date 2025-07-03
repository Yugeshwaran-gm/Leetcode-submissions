class Solution(object):
    def subarraySum(self, nums, k):
        co=0
        pre_sum=0
        prefix_map=defaultdict(int)
        prefix_map[0]=1
        for n in nums:
            pre_sum+=n
            if pre_sum-k in prefix_map:
                co+=prefix_map[pre_sum-k]
            prefix_map[pre_sum]+=1
        return co