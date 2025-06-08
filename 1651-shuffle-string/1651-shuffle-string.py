class Solution(object):
    def restoreString(self, s, i):
        re={}
        for j in range(len(i)):
            re[i[j]]=s[j]
        print(re)
        t=[re[k] for k in sorted(re)]
        # t=[re[k] for k in sorted(re)]
        return ''.join(t)