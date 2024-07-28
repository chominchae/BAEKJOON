N=int(input())
M=int(input())
matrix = [[0] * 2 for _ in range(M)]
linked=set()

for i in range(M):
    matrix[i][0],matrix[i][1]=map(int,input().split())
    if matrix[i][0]>matrix[i][1]:
        swap=matrix[i][0]
        matrix[i][0]=matrix[i][1]
        matrix[i][1]=swap

matrix = sorted(matrix)

for i in range(M):
    u=matrix[i][0]
    v=matrix[i][1]
    if u==1 or u in linked:
        linked.add(v)
    if v==1 or v in linked:
        linked.add(u)
        

for j in range(M-1,-1,-1):
    u=matrix[j][0]
    v=matrix[j][1]
    if u==1 or u in linked:
        linked.add(v)
    elif v==1 or v in linked:
        linked.add(u)
    
linked.discard(1)
print(len(linked))
