# https://www.acmicpc.net/problem/25501
# 재귀의 귀재

from io import StringIO
import sys

input_ex1 = """5
AAA
ABBA
ABABA
ABCA
PALINDROME"""
sys.stdin = StringIO(input_ex1)

def recursion(s, l, r):
    global r_cnt
    r_cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

while True:
  try:
    input = int(sys.stdin.readline())
    for _ in range(input):
       text = sys.stdin.readline().strip()
       r_cnt = 0
       cnt = isPalindrome(text)
       print(cnt, r_cnt)
  except:
    break
    