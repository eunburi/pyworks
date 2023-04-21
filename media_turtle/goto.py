#좌표이동
import turtle as t
import time
import random

t.shape('turtle')
'''
t.up()
time.sleep(1) #1초 대기
t.goto(0,150)
time.sleep(1)
t.goto(100,150)
time.sleep(1)
t.goto(0,0)
'''

#실행 시랜덤하게 보임
"""
x = random.randint(-250,250)
y = random.randint(-250,250)
t.up()
t.goto(x,y)
"""
#마음대로 걷는 거북이
t.speed(0)
t.shapesize(1)
for x in range(300):
    ang = random.randint(1,360) # 랜덤한 각도 저장
    t.setheading(ang)
    t.forward(70)

t.mainloop()