class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=set()
        col=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
                
        for it in row:
            matrix[it]=[0]*len(matrix[0]) 
        
        for co in col:
            for i in range(len(matrix)):
                matrix[i][co]=0
