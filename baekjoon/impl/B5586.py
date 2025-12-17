# https://www.acmicpc.net/problem/5586
# JOI와 IOI

from io import StringIO
import sys

# input_ex1 = """JOIJOI"""
# input_ex2 = """JOIOIOIOI"""
# input_ex3 = """JOIOIJOINXNXJIOIOIOJ"""

# sys.stdin = StringIO(input_ex3)

text = list(sys.stdin.readline())
text_arr = []

fir = "JOI"
sec = "IOI"

fir_answer = 0
sec_answer = 0

for num in range(len(text)):
    str_slice = text[num:num+3]
    str_text = ""

    if len(str_slice) == 3:
        str_text = "".join(str_slice)
        text_arr.append(str_text)
    else:
        break

for num in range(len(text_arr)):
    if text_arr[num] == fir:
        fir_answer += 1
    if text_arr[num] == sec:
        sec_answer += 1
    

print(fir_answer)
print(sec_answer)