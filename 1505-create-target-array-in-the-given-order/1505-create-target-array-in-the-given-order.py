class Solution(object):
    def createTargetArray(self, n, ie):
    #    if len(n)!=len
       t=[]
       for i in range(len(n)):
        t.insert(ie[i],n[i])
       print(t)
       return t