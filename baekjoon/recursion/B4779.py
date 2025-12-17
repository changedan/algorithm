# https://www.acmicpc.net/problem/4779
# 칸토어 집합

from io import StringIO
import sys

input_ex1 = """0
1
3
2"""
sys.stdin = StringIO(input_ex1)

arr = ['' for _ in range(13)]
arr[0] = '-'

for i in range(1, 13):
  arr[i] = arr[i - 1] + (" " * (3 ** (i - 1))) + arr[i - 1]

while True:
  try:
    input = int(sys.stdin.readline())
    print(arr[input])
  except:
    break
    
  