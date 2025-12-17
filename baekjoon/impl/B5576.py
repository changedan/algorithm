# https://www.acmicpc.net/problem/5576
# 콘테스트
from io import StringIO
import sys

ex_input = """23
23
20
15
15
14
13
9
7
6
25
19
17
17
16
13
12
11
9
5
"""

# sys.stdin = StringIO(ex_input)

input_range = 20
score_range = int(input_range // 2)
# 1 ~ 10줄 # 0을 11개 생성
# w 대학의 각 참가자의 점수
w_list = [0 for _ in range(score_range + 1)]

# 11 ~ 20줄 # 0을 11개 생성
# k 대학의 각 참가자의 점수
k_list = [0 for _ in range(score_range + 1)]

w_score = 0
k_score = 0

# 점수 입력받기 - w대학
for num in range(score_range):
    # 인덱스 0 버리기
    w_input = int(sys.stdin.readline().rstrip())
    w_list[num + 1] = w_input


w_list.sort()    
# print("w대학", w_list)

# 점수 입력받기 - k대학
for num in range(score_range):
    # 인덱스 0 버리기
    k_input = int(sys.stdin.readline().rstrip())
    k_list[num + 1] = k_input

k_list.sort()
# print("k대학", k_list)

for _ in range(3):
    w_score += w_list[10 - _]
    k_score += k_list[10 - _]

print(w_score, k_score)