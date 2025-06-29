class Solution(object):
    def sortSentence(self, s):
        t=list(s.split())
        print(t)
        d={}
        for i in range(len(t)):
            # print(s[i][-1])
            d[t[i][-1]]=t[i]
        print(d)
        return ' '.join([d[k][:-1] for k in sorted(d, key=int)])