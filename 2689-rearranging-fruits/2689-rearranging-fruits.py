class Solution:
    def minCost(self, ba1: List[int], ba2: List[int]) -> int:
        b1={}
        b2={}
        for i in range(len(ba1)):
            b1[ba1[i]]=b1.get(ba1[i],0)+1    
            b2[ba2[i]]=b2.get(ba2[i],0)+1    
        all_keys=set(b1.keys()) |set(b2.keys())
        for f in all_keys:
            tot=b1.get(f,0)+b2.get(f,0)
            if tot % 2!=0:
                return -1
        to_swap=[]
        for f in all_keys:
            diff=b1.get(f,0)-b2.get(f,0)
            if diff!=0:
                to_swap.extend([f]*(abs(diff)//2))
        to_swap.sort()
        glbmin=min(min(ba1),min(ba2))
        cost=0
        for i in range(len(to_swap)//2):
            cost+=min(to_swap[i],2*glbmin)
        return cost