# https://www.acmicpc.net/problem/3028
# 창영마을

from io import StringIO
import sys

input_ex1 = """AB"""
input_ex2 = """CBABCACCC"""

# !!
# sys.stdin = StringIO(input_ex2)

input_list = list(sys.stdin.readline())
answer_list = [1, 0, 0]

for num in range(len(input_list)):
    if input_list[num] == 'A':
        answer_list[0], answer_list[1] = answer_list[1], answer_list[0]
    elif input_list[num] == 'B':
        answer_list[1], answer_list[2] = answer_list[2], answer_list[1]
    elif input_list[num] == 'C':
        answer_list[2], answer_list[0] = answer_list[0], answer_list[2]

answer = answer_list.index(1)
print(answer + 1)
