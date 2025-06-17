class Solution(object):
    def countMatches(self, i, k, v):
        a,c=0,0
        if k=="type":
            a=0
        elif k=="color":
            a=1
        elif k=="name":
            a=2
        print(a)
        for j in range(len(i)):
            print(i[j][a])
            if (i[j][a])==v:
                c+=1
        return c