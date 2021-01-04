'''
A : 2D matrix containing 0s and 1s
N : Number of rows
M : Number of columns
'''
rowDirection    = [-1,-1,-1,0,0,1,1,1]
columnDirection = [-1,0,1,-1,1,-1,0,1]


def validateIndices(row,col,rowSize,colSize,arr):
    if row <0 or col < 0:
        return False
    if row >= rowSize or col >= colSize:
        return False
   
    if arr[row][col]!=1:
        return False
    return True
def findMaxArea(N, M, A):
   
    currRow= N-1
    currCol=M-1
    currMaxAtStage,resAtCurrentStage =[0,0]
    visited = [[0 for _ in range(M)]for _ in range(N) ]
    print("starting ",currRow,currCol)
    for i in range(len(rowDirection)):
        print("trying row :{} col: {}".format(currRow+rowDirection[i], currCol+columnDirection[i]))
        if  validateIndices(currRow, currCol,N,M,A):
            if  visited[currRow][currCol] ==0 :
                visited[currRow][currCol]=1
         
                resAtCurrentStage = 1+ findMaxArea(currRow+rowDirection[i], currCol+columnDirection[i], A)
                if resAtCurrentStage > currMaxAtStage:
                    currMaxAtStage =  resAtCurrentStage
               
        
    return currMaxAtStage+1
    
def printArray(arr):
    for i in arr:
        print(i)

            
        
        
        
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    r=int(line[0])
    c=int(line[1])
    line=input().strip().split()
    matrix=[ [0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):                                                                                                                                                                                                                                                                                                                                                                                                                          
            matrix[i][j] = int( line[i*c+j] )
    

    print(findMaxArea(r, c, matrix))
# } Driver Code Ends