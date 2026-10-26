import turtle as t
import random
import time

d = 0.1
s = 0
hs = 0
paused = False

sc = t.Screen()
sc.title("Snake Game")
sc.bgcolor("blue")
sc.setup(width=600, height=600)
sc.tracer(0)

h = t.Turtle()
h.shape("square")
h.color("white")
h.penup()
h.goto(0, 0)
h.direction = "Stop"

f = t.Turtle()
f.speed(0)
f.shape(random.choice(['square', 'triangle', 'circle']))
f.color(random.choice(['red', 'green', 'black']))
f.penup()
f.goto(0, 100)

p = t.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.penup()
p.hideturtle()
p.goto(0, 250)
p.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

btn = t.Turtle()
btn.speed(0)
btn.shape("square")
btn.shapesize(stretch_wid=1.2, stretch_len=4)
btn.color("white")
btn.penup()
btn.goto(-240, -265)

btn_label = t.Turtle()
btn_label.hideturtle()
btn_label.penup()
btn_label.color("black")
btn_label.goto(-240, -275)
btn_label.write("Pause", align="center", font=("candara", 14, "bold"))

pause_msg = t.Turtle()
pause_msg.hideturtle()
pause_msg.penup()
pause_msg.color("yellow")
pause_msg.goto(0, -60)
def toggle_pause(x=None, y=None):
    global paused
    paused = not paused
    btn_label.clear()
    pause_msg.clear()
    if paused:
        btn_label.write("Resume", align="center", font=("candara", 14, "bold"))
        pause_msg.write("PAUSED", align="center", font=("candara", 32, "bold"))
    else:
        btn_label.write("Pause", align="center", font=("candara", 14, "bold"))
def up():
    if h.direction != "down":
        h.direction = "up"
def down():
    if h.direction != "up":
        h.direction = "down"
def left():
    if h.direction != "right":
        h.direction = "left"
def right():
    if h.direction != "left":
        h.direction = "right"
def move():
    if h.direction == "up":
        h.sety(h.ycor() + 20)
    if h.direction == "down":
        h.sety(h.ycor() - 20)
    if h.direction == "left":
        h.setx(h.xcor() - 20)
    if h.direction == "right":
        h.setx(h.xcor() + 20)
def reset_game():
    global s, d
    time.sleep(1)
    h.goto(0, 0)
    h.direction = "Stop"
    f.goto(random.randint(-270, 270), random.randint(-270, 270))
    for segment in seg:
        segment.goto(1000, 1000)
    seg.clear()
    s = 0
    d = 0.1
    p.clear()
    p.write(f"Score : {s} High Score : {hs}", align="center", font=("candara", 24, "bold"))


sc.listen()
sc.onkeypress(up, "Up")
sc.onkeypress(down, "Down")
sc.onkeypress(left, "Left")
sc.onkeypress(right, "Right")
sc.onkeypress(toggle_pause, "p")
sc.onkeypress(toggle_pause, "space")
btn.onclick(toggle_pause)

seg = []

while True:
    sc.update()
    if paused:
        time.sleep(0.05)
        continue

    if h.xcor() > 290 or h.xcor() < -290 or h.ycor() > 290 or h.ycor() < -290:
        reset_game()

    if h.distance(f) < 20:
        f.goto(random.randint(-270, 270), random.randint(-270, 270))

        n_seg = t.Turtle()
        n_seg.speed(0)
        n_seg.shape("square")
        n_seg.color("orange")
        n_seg.penup()
        seg.append(n_seg)
        d -= 0.001
        s += 10
        if s > hs:
            hs = s
        p.clear()
        p.write(f"Score : {s} High Score : {hs}", align="center", font=("candara", 24, "bold"))

    for i in range(len(seg) - 1, 0, -1):
        x, y = seg[i - 1].xcor(), seg[i - 1].ycor()
        seg[i].goto(x, y)

    if len(seg) > 0:
        x, y = h.xcor(), h.ycor()
        seg[0].goto(x, y)

    move()

    for segment in seg:
        if segment.distance(h) < 20:
            reset_game()
            break

    time.sleep(d)
