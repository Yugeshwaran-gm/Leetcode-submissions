# import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        pq=[]
        for i in range(len(nums)):
            heapq.heappush(pq,-nums[i])
        for i in range(k):
            res=-heapq.heappop(pq)
        return res