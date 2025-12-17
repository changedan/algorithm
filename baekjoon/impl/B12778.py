# https://www.acmicpc.net/problem/12778
# CTP공국으로 이민 가자
# from io import StringIO
import sys

ex_input = """3
3 C
C T P
4 N
9 14 8 1
5 C
H E L L O
"""

# sys.stdin = StringIO(ex_input)

table = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# input_1
t = int(sys.stdin.readline())

for _ in range(t):
    answer = []

    # input_2
    m_list = list(map(str, sys.stdin.readline().split()))
    m = int(m_list[0])
    test_category = m_list[1]

    # input_3
    test_content = list(map(str, sys.stdin.readline().split()))

    if test_category == "C":
        for _ in range(m):
            test = test_content[_]
            idx = table.index(test)
            answer.append(idx + 1)

    if test_category == "N":
        for _ in range(m):
            test = int(test_content[_])
            string = table[test - 1]
            answer.append(string)
    
    print(*answer, sep= " ")
    