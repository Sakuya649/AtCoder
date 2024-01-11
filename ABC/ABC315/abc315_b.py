m = int(input())
d = list(map(int, input().split()))
mid = (sum(d)+1) / 2

for i in range(m):
    if d[i] >= mid:
        print(i+1, int(mid)) 
        break
    mid -= d[i]