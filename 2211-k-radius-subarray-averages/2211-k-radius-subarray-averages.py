class Solution(object):
    def getAverages(self, n, k):
        if k==0:
            return n
        if len(n)<(2*k+1):
            return [-1]*len(n)
        avgl=[-1]*len(n)
        prefix=[0]*(len(n)+1)
        for i in range(len(n)):
            prefix[i+1]=prefix[i]+n[i]
        for i in range(k,len(n)-k):
            tot=prefix[i+k+1]-prefix[i-k]
            avgl[i]=tot//(2*k+1)
        return avgl