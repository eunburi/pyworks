import turtle as t
import random

score = 0 # 점수
playing = False # 게임 실행 상태 변수

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

#주인공 거북이
t.setup(500, 500)
t.bgcolor('skyblue')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white')
t.shapesize(1)



#적 거북이
te = t.Turtle()
te.shape('turtle')
t.shapesize(1)
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

#먹이
tf = t.Turtle()
tf.shape('circle')
tf.color('blue')
tf.speed(0)
tf.up()
tf.goto(0, -200)

#키 조종
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, 'space')
t.listen()
message("Turtle Run", "[Space]")

def play():
    global score
    global playing
    t.forward(10)
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)

#주인공 거북이가 적 거북이에 닿으면 게임 종료
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

#주인공 거북이가 먹이에 닿으면 점수가 올라감
    if t.distance(tf) < 12:
        score = score + 1
        t.write(score)
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        tf.goto(start_x, start_y)

#게임 실행(0.1초 콜백)
    if playing:
        t.ontimer(play, 100)

t.mainloop()



