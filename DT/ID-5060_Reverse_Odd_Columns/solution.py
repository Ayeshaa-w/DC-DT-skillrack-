n=int(input())
matrix=[]
for i in range(n):
  val=list(map(int,input().split())
  matrix.append(val)
for i in range(n//2):
  for j in range(n):
    if j%2==0:
      matrix[i][j],matrix[n-i-1][j]=matrix[n-i-1][j],matrix[i][j]
for i in range(n):
  for j in range(n):
    print(matrix[i][j],end=" ")
  print()
           
           
           
          
