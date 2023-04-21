#거북이 대포 게임
''''
1.키보드 방향키로 발사 각도 조절
2. 화살촉 모양의 포탄이 하늘로 날아감
3. 스페이스바로 발사
'''

import turtle as t
import random

def turn_up(): #위 쪽 화살표 키
    t.left(2)

def turn_down(): #아래 쪽 화살표 키
    t.right(2)

def fire():
    ang = t.heading() #거북이가 바라보는 현재 각도
    while t.ycor() > 0: # y좌표가 0보다 크면 - 포탄이 땅 위에 있는 동안
        t.forward(15)
        t.right(5)
    d =t.distance(target,0)
    t.write(d)
    t.sety(random.randint(10,100)) # y좌표 - 성공 또는 실패를 표시할 위치
    if d < 25: #명중 - 목표지점에 닿음
        t.color('blue')
        t.write('Good!',False, "center",("",15))
    else: #목표 지점에 닿지 않았을때
        t.color('red')
        t.write('Bad!', False, "center",("",15))
        t.color('black')
        t.goto(-200,10)
        t.setheading(ang) # 기억된 머리 각도 설정



#땅 그리기
t.goto(-300,0)
t.goto(300,0)

#목표 지점 설정
target = random.randint(50,150) #50~150 사이에 x좌표 한 지점
t.color('green')
t.pensize(2)

#목표 지점의 길이 - 50px
t.goto(target-25,1) # target = 50, 100-25 = 75
t.down()
t.goto(target+25,1) # target = 50, 500+25 = 75

#포탄의 처음위치
t.color('black')
t.up()
t.goto(-200,10)
t.setheading(20)

#거북이 대포가 동작하는 데 필요한 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire, "space") #스페이스 키 누르면 발사
t.listen()


t.mainloop()






t.mainloop()