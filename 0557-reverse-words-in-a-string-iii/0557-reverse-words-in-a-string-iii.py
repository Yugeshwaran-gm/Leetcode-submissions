class Solution(object):
    def reverseWords(self, s):
        a=[]
        b=[]
        a=s.split(" ")
        print(a)
        for i in range(len(a)):
           b.append(a[i][::-1])
        return " ".join(b) 