n = int(input())
d, x = map(int, input().split())
A_list = [int(input()) for i in range(n)]
for a in A_list:
    x += 1
    if a <= d:
        x += (d-1)//a
print(x)