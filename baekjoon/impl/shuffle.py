import sys
import random
from io import StringIO
import itertools

input_n = """100"""

sys.stdin = StringIO(input_n)

n = int(sys.stdin.readline())
random_n = random.randint(0, n)
random_list = []
arr = []

for _ in range(n):
    random_list.append()


print(random_list)

import sys
import random
from io import StringIO

input_n = """100"""
sys.stdin = StringIO(input_n)

n = int(sys.stdin.readline())

# arr에 초기 데이터 넣기
arr = list(range(n))

# arr를 직접 섞기
random.shuffle(arr)

print(arr)