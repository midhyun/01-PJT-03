import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for test_case in range(1, T+1):

    people = int(input())                       # 사람의 수
    lst_earn = list(map(int, input().split()))  # 사람들의 소득 리스트
    avg_earn = float(sum(lst_earn)/people)      # 소득 평균

    result_cnt = 0                              # 소득이 평균이하인 사람들의 수
    for earn in lst_earn:                       # 각 소득이 평균 이하일 경우
        if earn <= avg_earn:
            result_cnt += 1                     # 결과값에 카운트
    print(f'#{test_case} {result_cnt}')