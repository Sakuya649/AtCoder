from re import A


n = int(input())
A_list = input().split()
A_list = [int(a) for a in A_list]

sm = 0
x = 0
for i in range(n):
    sm += abs(x - A_list[i])
    x = A_list[i]
sm += abs(x)

for i in range(n):
    a = 0
    if i != 0:
        a = A_list[i-1]
    b = A_list[i]
    c = 0
    if i != n-1:
        c = A_list[i+1]
    ans = sm
    ans -= abs(a-b)
    ans -= abs(b-c)
    ans += abs(a-c)
    print(ans)