def zeroMatrix(matrix, n, m):
    # Write your code here.
    x=[[],[]]
    con=False
    i=0
    while i<n:
        j=0
        while j<m:
            if matrix[i][j]==0 and con==False:
                x[0].append(i)
                x[1].append(j)

            if con==True and (i in x[0] or j in x[1]):
                matrix[i][j]=0
            j+=1

        if i==n-1 and con==False:
            con=True
            i=-1 
        i+=1
    return matrix
print(zeroMatrix([[2,4,3],[1,0,0]],2,3))