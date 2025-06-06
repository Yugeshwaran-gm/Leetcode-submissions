class Solution(object):
    def maximumWealth(self, a):
        m=0
        for i in range(len(a)):
            row=0
            for j in range(len(a[i])):
                row+=a[i][j]
            if(row>m):
                m=row
        return m