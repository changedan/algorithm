# https://www.acmicpc.net/problem/4597
# 패리티
from io import StringIO
import sys

ex_input = """101e
010010o
1e
000e
110100101o
#
"""

# 제출할 때 주석 처리
# sys.stdin = StringIO(ex_input)

# 1이 없는 비트 스트링 => 짝수 패리티
# 1이 없는 비트 스트링은 짝수 패리티

# input
while True:
    input_string = sys.stdin.readline().rstrip()

    if input_string == '#':
        break

    input_list = [input_string[ele] for ele in range(len(input_string))]
    count = 0

    for _ in range(len(input_list)):
        if input_list[_] == '1':
            count += 1

    # 1의 개수가 짝수개 => 짝수 패리티    
    if input_list[-1] == 'e':
        if count == 0:
            input_list[-1] = '0'
        elif count % 2 == 0:
            input_list[-1] = '0'
        elif count % 2 == 1:
            input_list[-1] = '1'

    # 1의 개수가 홀수개 => 홀수 패리티
    if input_list[-1] == 'o':
        if count % 2 == 0:
            input_list[-1] = '1'
        elif count % 2 == 1:
            input_list[-1] = '0'

    print(*input_list, sep = "")