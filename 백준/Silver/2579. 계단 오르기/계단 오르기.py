n = int(input())
s = [ int(input()) for _ in range(n) ]
d = [-1] * n

d[0] = s[0]
if n > 1:
    d[1] = s[0] + s[1]
if n > 2:
    d[2] = max(s[0], s[1]) + s[2]

for i in range(3, n):
    d[i] = max(d[i-2], s[i-1] + d[i-3]) + s[i]

print(d[n-1])

