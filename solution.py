n=int(input())
matrix=[]
for i in range(n):
  val=list(map(int,input().split()))
  matrix.append(val)
d1=set()
d2=set()
for i in range(n):
  d1.add(matrix[i][i])
col=n-1
for i in range(n):
  d2.add(matrix[i][col])
  col-=1
if d1==d2:
  print("yes")
else:
  print("no")
