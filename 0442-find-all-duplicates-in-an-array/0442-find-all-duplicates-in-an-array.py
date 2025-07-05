class Solution(object):
    def findDuplicates(self, nums):
        # duplicate={}
        # r=[]
        # for num in nums:
        #     duplicate[num]=duplicate.get(num,0)+1
        # print(duplicate)
        # for key,value in duplicate.items():
        #     if value>1:
        #         r.append(key)
        # return r
        result=[]
        for num in nums:
            idx=abs(num)-1
            if nums[idx]<0:
                result.append(abs(num))
            else:
                nums[idx]*=-1
        return result