# 일기 암호화하기
import sys

# 1. 입력
words = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()

# 2. 표 - 평문
# table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
table = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

new_table = []

# 3. words에서 반복되는 글자 제거
for w in words:
  if w in list(new_table):
    continue
  new_table.append(w)

# 4. 암호표 만들기
for w in table:
  if w in list(new_table):
    continue
  new_table.append(w)

# 5. 입력받은 글자를 암호로 변환
result = ""
for s in key:
  num = table.index(s)
  result += new_table[num]

print(result)