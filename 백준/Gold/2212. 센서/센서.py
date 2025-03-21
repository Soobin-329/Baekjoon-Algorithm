# 센서
# 골드 5

import sys
input = sys.stdin.readline


n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

dist = []

for i in range(len(sensors)- 1):
    dist.append(sensors[i+1]-sensors[i])

dist.sort()

answer = sum(dist[:(len(dist)-(k-1))])

print(answer)