class Solution(object):
    def subtractProductAndSum(self, n):
        p=1
        a,d=0,0
        while(n!=0):
            d=n%10
            p*=d
            a+=d
            n/=10
        return p-a