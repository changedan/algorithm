# https://www.acmicpc.net/problem/10870
# 피보나치 수 5

from io import StringIO
import sys

# input_ex1 = """10"""
# sys.stdin = StringIO(input_ex1)

input_n = int(sys.stdin.readline())

def fibo(n):
  if n == 1:
    return 1
  if n == 0:
    return 0

  return fibo(n - 1) + fibo(n - 2)

print(fibo(input_n))