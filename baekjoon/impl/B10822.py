# https://www.acmicpc.net/problem/10822
# 더하기
import sys

num_input = list(map(int, sys.stdin.readline().split(",")))
sum = 0

for num in num_input:
    sum += num

print(sum)