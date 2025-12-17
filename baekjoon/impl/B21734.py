# https://www.acmicpc.net/problem/21734
# SMUPC의 등장
from io import StringIO
import sys

# 입력
# input_ex1 = """smupc"""
# sys.stdin = StringIO(input_ex1)

input_text = list(sys.stdin.readline())

#  아스키코드

for num in range(len(input_text)):
    num_arr = list(str(ord(input_text[num])))
    t_num = 0
    
    for n in range(len(num_arr)):
        number_str = num_arr[n]
        t_num += int(number_str)
    
    answer = input_text[num] * t_num
    print(answer)