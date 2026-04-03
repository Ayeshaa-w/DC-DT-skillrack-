s=list(map(str,input().split())
for i in range(len(s)):
  for j in range(len(s[i])):
    if j%2==0:
      print(s[i][j].upper(),end="")
    else:
      print(s[i][j].lower(),end="")
  print(end=" ")
