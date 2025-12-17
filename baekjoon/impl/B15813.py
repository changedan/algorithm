# 너의 이름은 몇점이니
import sys

# 1. 이름 길이 / 이름
name_len = sys.stdin.readline().split() # 100이하
name = sys.stdin.readline().strip() # len(name) < 101
name_s = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# 2. 점수 계산
score = 0
for n in name:
  score += name_s.index(n) + 1

print(score)