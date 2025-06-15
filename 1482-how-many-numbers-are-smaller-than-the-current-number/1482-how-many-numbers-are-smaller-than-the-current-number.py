class Solution(object):
    def smallerNumbersThanCurrent(self, n):
        b=[]
        for i in range(len(n)):
            c=0
            for j in range(len(n)):
                if i==j:
                    continue
                elif n[i]>n[j]:
                    c+=1
            b.append(c)
        print(b)
        return b