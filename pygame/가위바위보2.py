# 가위바위보 게임

import random

print("★가위 바위 보☆")
가위바위보 = ['가위','바위','보']

def play(you, com):
    if you not in 가위바위보:  # x in y문
        print("잘못된 입력입니다. 다시 입력해 주세요")
        return

    #비긴경우, 이긴경우, 진 경우
    if you == com:
        state = 0
    elif you == '가위' and com == '보':
        state=2
    elif you == '바위' and com == '가위':
        state=2
    elif you == '보' and com == '바위':
        state=2
    else:
        state=1

result = {0:'무승부', 1:'패', 2:'승'}
print(result[state])
state = 0

you = input("당신 :")
#random choice() 사용ㄹ
com = random.choice(가위바위보)
print("컴퓨터 : ", com)