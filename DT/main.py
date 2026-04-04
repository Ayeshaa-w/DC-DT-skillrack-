def has_even_digits(num):
    return len(str(abs(num))) % 2 == 0

n = int(input())
arr = list(map(int, input().split()))

result = [x for x in arr if has_even_digits(x)]
print(*result)