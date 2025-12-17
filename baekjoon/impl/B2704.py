# https://www.acmicpc.net/problem/2704
# 이진법 시계
import sys

# 테스트 케이스의 수
n = int(sys.stdin.readline())
two_range = 5

# 테스트 케이스
for test_case in range(n):
    time_arr = list(map(int, sys.stdin.readline().split(":")))
    
    v_arr = [[0] * 3 for _ in range(6)]  # 6행 3열
    h_arr = [[0] * 6 for _ in range(3)]  # 3행 6열

    for time_num in range(3):
        number = time_arr[time_num]
        
        for num in range(6):
            j = 5 - num
            mock = 2 ** j

            if number >= mock:
                number -= mock
                v_arr[num][time_num] = 1
                h_arr[time_num][num] = 1
            else:
                v_arr[num][time_num] = 0
                h_arr[time_num][num] = 0

    v_str = "".join(str(v_arr[i][j]) for i in range(6) for j in range(3))
    h_str = "".join(str(h_arr[i][j]) for i in range(3) for j in range(6))
    print(v_str, h_str)