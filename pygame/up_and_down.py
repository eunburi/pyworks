# 숫자 추측게임
'''
게임방법
- 게임이 시작되면 컴퓨터가 난수(정답)를 생성한다.
- 사용자의 추측값이 정답과 같으면 '정답',
 추측값이 정답보다 크면 "너무 커요!"
 추측값이 정답보다 작으면 '너무 작아요!' 출력

'''

import random

#컴퓨터의 난수생성
com = random.randint(1,100)
min_v = 1
max_v = 100
"""
while True:
    guess = int(input(f"맞혀보세요({min_v}~{max_v}) > "))
    # 조건문 작성
    if guess == com:
        print(f"정답! {com}")
        break
    elif guess > com:
        print("너무 큽니다")
        max_v = guess
    else:
        print("너무 작습니다")
        min_v = guess
"""

try:
    for i in range(0,10):
        guess = int(input(f"맞혀보세요({min_v}~{max_v}) > "))
        # 조건문 작성
        if guess > 100 or guess < 1:
            print("입력범위가 아닙니다.")
        elif guess == com:
            print(f"정답! {com}")
            break
        elif guess > com:
            print("너무 큽니다")
            max_v = guess
        else:
            print("너무 작습니다")
            min_v = guess
except:
    print("숫자를 입력하세요")


print(f"점수 : {(10-i) * 10}점")





