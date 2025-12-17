# 직사각형 네 개의 합집합의 면적 구하기
import sys

# 1. 100 * 100 보드
board = [[0] * 100 for _ in range(100)]

result = 0
# 2. x1, y1, x2, y2 받기 > 4번
for _ in range(4):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  for x in range(x1, x2):
    for y in range(y1, y2):
      # 3. 해당하는 좌표를 1로 변경
      if (board[x][y] == 1):
        continue
      board[x][y] = 1
      # 4. 1을 합산
      result += 1

print(result)