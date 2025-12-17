# 나머지
import sys

arr = [int(sys.stdin.readline()) for _ in range(10)]
new_arr = []

for i in range(len(arr)):
  num = arr[i] % 42
  if num in new_arr:
    continue
  else:
    new_arr.append(num)

print(len(new_arr))