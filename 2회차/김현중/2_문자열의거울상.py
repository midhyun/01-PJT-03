import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for test_case in range(1, T+1):         # 거울의 경우 좌우가 대칭됨, // 순서는 역순으로, 알파벳은 각각 뒤집는다.
    sent = input()
    sent = sent.replace('d','a')        # 'b' 를 'd' 로 뒤집을때 'd'는'b'로 뒤집혀야 하는데 동시에 작업할 수 없어서 'a'로 임시변환.
    sent = sent.replace('b','d')
    sent = sent.replace('a','b')        # 임시로 'a'로 바꾼 'd'를 'b' 로 변환
    sent = sent.replace('p','a')        # 이하 동
    sent = sent.replace('q','p')
    sent = sent.replace('a','q')
    sent_mir = sent[::-1]
    print(f'#{test_case} {sent_mir}')