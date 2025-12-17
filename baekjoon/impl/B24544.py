# 카카오뷰 큐레이팅 효용성 분석
import sys

ex_input = """3
1000 20 11
1 0 0
"""

# 콘텐츠 개수 N
N = int(sys.stdin.readline())
# 콘텐츠 N에 대한 흥미도
N_interest = list(map(int, sys.stdin.readline().split()))
# 콘텐츠 N의 등록 여부
enroll = list(map(int, sys.stdin.readline().split()))

arr = list(zip(N_interest, enroll))
# todo : list -> refac
new_arr = [0, 0]

for i in range(N):
  new_arr[0] += arr[i][0]
  if (arr[i][1] == 0):
    new_arr[1] += arr[i][0]

# todo : refac
# print(new_arr[0])
# print(new_arr[1])
print(*new_arr, sep="\n")