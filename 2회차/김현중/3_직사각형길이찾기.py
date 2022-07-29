import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for test_case in range(1, T+1):                 # 직사각형의 3변의 길이를 square 변수에 리스트로 저장.
    square = list(map(int, input().split()))    
    if square.count(square[0]) == 1:            # 저장된 리스트의 첫번째 값이 1개 들어있으면 나머지 두개값은 평행 변이므로 길이가 같다.
        print(f'#{test_case} {square[0]}')      # 구하고자 하는 나머지 변의 길이는 첫번째 값과 같다.
    elif square.count(square[1]) == 1:          # 두번째 값이 1개 들어있으면 나머지 두개 값은 평행 변이므로 길이가 같다.
        print(f'#{test_case} {square[1]}')      # 따라서 나머지 변의 길이는 두번째 값과 같다.
    else: print(f'#{test_case} {square[2]}')    # 1, 2 모두 아니라면 세번째 값과 같다.