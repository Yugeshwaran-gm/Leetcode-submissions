class Solution(object):
    def maxDepth(self, s):
        li=list(s)
        print(li)
        count=0
        depth=0
        for i in range(len(li)):
            if li[i]=="(":
                count+=1
            elif li[i]==")":
                depth=max(depth,count)
                count-=1
            else:
                continue
        return depth