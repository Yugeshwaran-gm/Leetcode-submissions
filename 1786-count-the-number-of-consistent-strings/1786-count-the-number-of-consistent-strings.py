class Solution(object):
    def countConsistentStrings(self, a, w):
        als=set(a)
        c=0
        for wo in w:
            if all(c in a for c in wo):
                c+=1
        return c
