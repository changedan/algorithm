# https://www.acmicpc.net/problem/1316
# 그룹단어체커
import sys

# 단어 개수 n
# 0 < n < 101
n = int(sys.stdin.readline())

# 단어 n개 입력
word_arr = [sys.stdin.readline().split()[0] for _ in range(n)]
result = 0

for i in word_arr :
  prev = i[0]
  prev_save = []
  isGroupWord = True

  for j in range(len(i)):
    if i[j] != prev:
      prev_save.append(prev)

    if i[j] in prev_save:
      isGroupWord = False
      break # 즉시 판단 종료해야하므로 continue 사용 불가

    # print("i[j]", i[j])
    prev = i[j]
    # print("prev", prev)
    # print("prev_save", prev_save)

  if isGroupWord:
    result += 1
  # print("prev", prev)
  # print("prev_save", prev_save)

print(result)
