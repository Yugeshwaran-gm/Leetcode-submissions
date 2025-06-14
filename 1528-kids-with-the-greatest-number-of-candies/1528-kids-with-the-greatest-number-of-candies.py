class Solution(object):
    def kidsWithCandies(self, c, ec):
        m=0
        a=[]
        for i in range(len(c)):
            m=max(m,c[i-1])
        t=c.index(m)
        print(m,t)
        for i in range(len(c)):
            b=c[i]+ec
            if b>=m:
                a.append(True)
            else:
                a.append(False)
        return a
