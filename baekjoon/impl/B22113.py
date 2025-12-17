# https://www.acmicpc.net/problem/22113
# 창영이와 버스
import sys

# 도시에 존재하는 버스의 개수 N, 창영이가 이용하는 버스의 개수 M
n, m = map(int, sys.stdin.readline().split())

# 환승해야하는 버스 순서 (m개)
m_bus = list(map(int, sys.stdin.readline().split()))

# n줄, s번쨰 A_{S, E}
payment_list = [[0] * n for _ in range(n)]

# 요금 계산
answer = 0 

# 환승 요금
for payment in range(n):
    payment_list[payment] = list(map(int, sys.stdin.readline().split()))

# 환승 요금 계산
for num in range(m - 1):
    fir = m_bus[num]
    two = m_bus[num + 1]
    # print("fir", fir)
    # print("two", two)
    # print(payment_list[fir - 1][two - 1])
    answer += payment_list[fir - 1][two - 1]

print(answer)
