class Solution(object):
    def numberOfSteps(self, num):
        c=0
        d=num
        while d>0:
            if d%2==0:
                d=d//2
                print(d)
                c+=1
            else:
                d-=1
                print(d)
                c+=1
        return c