import turtle as t
import json as j
from sys import exit

FILE = 'web-likes/webbing'
SCALE = 2
screen = t.Screen()
screen.yscale, screen.xscale = screen.yscale * SCALE, screen.xscale * SCALE
t.title('Sistemas L')
pen = t.Turtle()
pen.color("#00ff40")
t.bgcolor("#2C2C2C")
pen.speed(100000)
pen.pen(shown=False)
pen.pensize(0.5)

with open(f'./{FILE}.json', 'r') as f:
    temp = j.load(f)
w = temp['AXIOM']
ALPHABET = temp['ALPHABET']
ROLL_RULES = temp['ROLL_RULES']
DRAW_RULES = temp['DRAW_RULES']

rollcount = 0
done = False

def close():
    global done
    done = True

def rolls(w:str, times:int = 1):
    for _ in range(times):
        w = roll(w)
    return w

def roll(w:str):
    temp = ''
    for x in w:
        temp += ROLL_RULES[x]
    return temp

def do(w:str):
    for x in w:
        if done:
            break
        temp = DRAW_RULES[x]
        if temp[0] == 'l':
            pen.left(int(temp.removeprefix('l')))
        elif temp[0] == 'r':
            pen.right(int(temp.removeprefix('r')))
        elif temp[0] == 'm':
            pen.forward(int(temp.removeprefix('m')))

def start(*args):
    global w
    pen.right(pen.heading())
    pen.penup()
    pen.goto(args)
    pen.pendown()
    do(w)

def zout():
    screen.xscale -= 0.1
    screen.yscale -= 0.1

def zin():
    screen.xscale += 0.1
    screen.yscale += 0.1

screen.onkey(zout, 'Up')
screen.onkey(zin, 'Down')
screen.listen()

w = rolls(w, 10)
screen.onclick(start)

t.onkeypress(close, 'Escape')

t.mainloop()
exit()