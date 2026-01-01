# https://www.acmicpc.net/problem/6603
# 로또

from io import StringIO
import sys

input_ex1 = """7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""
sys.stdin = StringIO(input_ex1)

def comb(idx, level):
  global select, arr, k

  if level == 6:
    for _ in select:
      print(_, end = " ")
    print()
    return
  
  for i in range(idx, k):
    select.append(arr[i])
    comb(i + 1, level + 1)
    select.pop()

while True:
  select = []
  input_lst = list(map(int, sys.stdin.readline().split(" ")))
  k = input_lst[0]
  arr = input_lst[1:]

  # input[0] == 0
  if k == 0:
    break

  # input[0] != 0
  comb(0, 0)
  print()
