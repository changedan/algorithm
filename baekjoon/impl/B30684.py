# https://www.acmicpc.net/problem/30684
# 모르고리즘 회장 정하기

from io import StringIO
import sys

input_ex1 = """7
KGW
LH
AHC
LKY
DREAM
AA
KTY
"""

# sys.stdin = StringIO(input_ex1)
n = int(sys.stdin.readline())
name_list = []
new_list = []

for _ in range(n):
    name_list.append(sys.stdin.readline().rstrip())

# print(name_list)
    
for _ in range(len(name_list)):
    if len(name_list[_]) != 3:
        continue

    new_list.append(name_list[_])
    
# print(new_list)
answer = sorted(new_list)
print(answer[0])