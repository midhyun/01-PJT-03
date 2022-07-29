import sys

sys.stdin = open("_암호문1.txt")

T = 10
for test_case in range(1, T+1):
    password_len = int(input())                 # 패스워드의 길이
    password = input().split()                  # 패스워드를 공백으로 구분해 리스트에 담음.
    order_insert_cnt = int(input())             # 입력하는 삽입명령어 개수
    order_inserts = input().split('I')          # 삽입 명령어를 'I' 로 구분해 리스트에 담음.

    for i in range(1, order_insert_cnt + 1):    # 첫번째 삽입 명령어는 '' 공백이므로 인덱스 1부터 순회함.
        insert = order_inserts[i].split()       # insert[0] == 삽입을 시작하는 인덱스, insert[1] == 삽입하는 order_inserts의 길이, insert[2:] == 삽입하는 암호문 
        password = password[:int(insert[0])] + insert[2:] + password[int(insert[0]):]
                                                # 기존 패스워드 x-1 번째 까지 + 삽입패스워드 + 기존패스워드의 x부터 == 기존패스워드 사이에 삽입하고자 하는 인덱스에 삽입
    print(f'#{test_case}', end = ' ')           # 기존 패스워드 값에 명령어에 따른 값을 삽입한 값으로 초기화 해줌.
    for i in range(10):
        print(password[i], end = ' ')
    print()