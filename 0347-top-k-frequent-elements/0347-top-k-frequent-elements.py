class Solution(object):
    def topKFrequent(self, nums, k):
        # if len(nums)==k:
        #     return nums
        res_dict={}
        for n in nums:
            res_dict[n]=res_dict.get(n,0)+1
        print(res_dict)
        sort_item=sorted(res_dict.items(),key=lambda x: x[1], reverse=True)
        print(sort_item)
        return [i[0] for i in sort_item[:k]]