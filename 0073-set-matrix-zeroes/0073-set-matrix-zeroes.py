class Solution(object):
    def setZeroes(self, matrix):
        rl=len(matrix)
        cl=len(matrix[0])
        fr,fc=False,False
        for i in range(rl):
            for j in range(cl):
                if(matrix[i][j]==0):
                    if i==0:
                        fr=True
                    if j==0:
                        fc=True
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,rl):
            for j in range(1,cl):
                if (matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
        if fr:
           for j in range(cl):
                matrix[0][j]=0
        if fc:
            for i in range(rl):
                matrix[i][0]=0
        return matrix