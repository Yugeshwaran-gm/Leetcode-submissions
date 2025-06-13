class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        j=list(jewels)
        s=list(stones)
        print(j,s)
        c=0
        for i in range(len(j)):
            for k in range (len(s)):
                if (j[i]==s[k]):
                    c+=1
        return c