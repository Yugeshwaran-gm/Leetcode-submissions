class Solution(object):
    def countConsistentStrings(self, a, w):
        als=set(a)
        ch=0
        for wo in w:
            if all(c in a for c in wo):
                ch+=1
        return ch
