class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        Premap={i:[] for i in range(n)}
        for c,p in pre:
            Premap[c].append(p)
        vs=set()
        def dfs(c):
            if c in vs:
                return False
            if Premap[c]==[]:
                return True
            vs.add(c)
            for p in Premap[c]:
                if not dfs(p): return False
            vs.remove(c)
            Premap[c]=[]
            return True
        print(Premap)
        for c in range(n):
            if not dfs(c): return False
        return True