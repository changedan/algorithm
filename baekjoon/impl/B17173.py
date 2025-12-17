# https://www.acmicpc.net/problem/17173
# 배수들의 합
import sys

n, m = map(int, sys.stdin.readline().split())

# m개의 정수 k
k_list = list(map(int, sys.stdin.readline().split()))
sum_list = []

for num in range(m):    
    k = k_list[num]
    mock = n // k

    for _ in range(mock):
        number = k * (_ + 1)
        
        if number not in sum_list:
            sum_list.append(number)
        
answer = sum(sum_list)
print(answer)