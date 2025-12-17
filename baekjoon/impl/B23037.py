# https://www.acmicpc.net/problem/23037
# 5의 수난
import sys

num_input = list(map(int, sys.stdin.readline().strip()))
sum = 0

for num in num_input:
    sum += num * num * num * num * num

print(sum)