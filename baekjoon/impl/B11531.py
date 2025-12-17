# https://www.acmicpc.net/problem/11531
# ACM 대회 채점 다국어

from io import StringIO
import sys

input_ex1 = """3 E right
10 A wrong
30 C wrong
50 B wrong
100 A wrong
200 A right
250 C wrong
300 D right
-1
"""

input_ex2 = """7 H right
15 B wrong
30 E wrong
35 E right
80 B wrong
80 B right
100 D wrong
100 C wrong
300 C right
300 D wrong
-1
"""

# sys.stdin = StringIO(input_ex2)
solved_count = 0
penalty = 0
solved_list = []

while True:
    log_list = list(sys.stdin.readline().split())
    search_text = ""
    penalty_arr = []
    wrong_acount = 0

    if log_list[0] == '-1':
        break

    solved_list.append(log_list)
    m = log_list[0]
    problem_name = log_list[1]
    problem_result = log_list[2]
    
    if problem_result == 'right':
        solved_count += 1
        search_text = problem_name
        # print(search_text)

    for _ in range(len(solved_list)):
        if search_text == solved_list[_][1]:
            penalty_arr.append(solved_list[_])

    for _ in range(len(penalty_arr)):
        if penalty_arr[_][2] == 'wrong':
            wrong_acount += 1
        if penalty_arr[_][2] == 'right':
            score = penalty_arr[_][0]
            penalty += int(score)
        
    penalty += wrong_acount * 20

print(solved_count, penalty)