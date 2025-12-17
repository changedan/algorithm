# https://www.acmicpc.net/problem/10708
# 크리스마스 파티
import sys

# 크리스마스 파티 - 점수 계산 게임
# 게임 규칙:
# 1. 각 게임마다 "타겟" 번호가 정해짐
# 2. 모든 친구들은 타겟이 누구인지 예상해서 번호를 외침
# 3. 점수 부여:
#    - 타겟을 맞춘 사람: 1점
#    - 타겟 본인: 타겟을 못 맞춘 사람 수만큼 점수 획득

# 친구 수 입력 (1번부터 n번까지)
# 3 <= n <= 100
n = int(sys.stdin.readline())

# 게임 횟수 입력
# 3 <= m <= 100
m = int(sys.stdin.readline())

# 각 게임의 타겟 번호 리스트 (m개)
# 예: [2, 3, 1] -> 1번 게임 타겟은 2번, 2번 게임 타겟은 3번, 3번 게임 타겟은 1번
target_list = list(map(int, sys.stdin.readline().split()))

# N명의 친구 점수를 0으로 초기화 (인덱스 0 = 1번 친구)
score_list = [0] * n

# m개의 게임을 순회하며 점수 계산
for game_num in range(m):
  # 현재 게임의 타겟 번호 (실제 친구 번호)
  current_target = target_list[game_num]

  # 현재 게임에서 각 친구들이 외친 번호 (n개)
  # 예: [2, 2, 1] -> 1번 친구는 2번을, 2번 친구는 2번을, 3번 친구는 1번을 외침
  select_num_list = list(map(int, sys.stdin.readline().split()))

  # 타겟을 못 맞춘 사람들의 수를 세기 위한 변수
  not_answer_count = 0

  # 각 친구가 외친 번호를 확인하여 타겟을 못 맞춘 사람 수 계산
  for selected_num in select_num_list:
    if selected_num != current_target:
      not_answer_count += 1

  # 점수 부여 1: 타겟을 맞춘 친구들에게 1점씩 부여
  for friend_idx in range(n):
    if select_num_list[friend_idx] == current_target:
      score_list[friend_idx] += 1

  # 점수 부여 2: 타겟 본인에게 "못 맞춘 사람 수"만큼 점수 부여
  # current_target은 1부터 시작하므로 -1을 해서 인덱스로 변환
  score_list[current_target - 1] += not_answer_count

# 각 친구의 최종 점수를 출력 (1번 친구부터 n번 친구까지)
for _ in score_list:
  print(_)