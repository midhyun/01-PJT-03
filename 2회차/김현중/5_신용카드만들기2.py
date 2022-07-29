import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T+1):
    card_mk = False
    card_num = input().replace('-','')                                  # 입력받은 값에서 '-'를 모두 제거해준다.
    z = card_num[0]

    if len(card_num) == 16:                                             # 카드번호는 총 16자리이고,
        if z == '3' or z == '4' or z == '5' or z == '6' or z == '9':    # 시작값이 3,4,5,6,9 중 하나여야 한다.
            card_mk = True                                              # 위 조건에 해당하면 True
    print(f'#{test_case} {card_mk*1}')                                  # True * 1 = 1, False * 1 = 0