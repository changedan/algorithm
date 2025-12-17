# 야바위 대장
import sys

# 1. 문자열 s 받기
s = sys.stdin.readline()
# 2. 숫자 t 받기
t = int(sys.stdin.readline())

s_list = list(s)

# 0 < s <= 100
# 0 < t <= 50

# t번 swap
for _ in range(t):
  # t번 입력 받기
  t_fir, t_sec = map(int, sys.stdin.readline().split())
  # swap
  s_list[t_fir], s_list[t_sec] = s_list[t_sec], s_list[t_fir]
    
# string 
# todo : join -> refac
result = ''.join(s_list)

print(result)