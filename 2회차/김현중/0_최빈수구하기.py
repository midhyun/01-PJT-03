import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())                                                                                        # Test_case
for test_case in range(T):

    case_num = int(input())                                                                             # input() 정리
    scores = list(map(int, input().split()))                                                            # 점수들을 정수형으로 리스트에 각각 담아줌.
    score_dict = {}
    

    for i in scores:                                                                                    # 점수의 개수를 카운트해서 딕셔너리에 추가함.
        score_dict[i] = score_dict.get(i, 0) + 1

    mod = sorted([k for k, v in score_dict.items() if max(score_dict.values()) == v],reverse = True)    # 개수가 가장 많은 점수를 정렬해서 가장큰 점수의 인덱스 == 0;
    print(f'#{case_num} {mod[0]}')
