n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    num = abs(i)
    digits = 0
    
    if num == 0:
        digits = 1
    else:
        while num > 0:
            digits += 1
            num //= 10

    if digits % 2 == 0:
        print(i, end=" ")