import turtle
hung_screen = turtle.Screen()
cb = turtle.Turtle()
hung_screen.bgcolor("black")
cb.speed(0)
count = 0
color = ''
vonglap = 0
while vonglap < 36:
    if vonglap == 0 or vonglap == 6 or vonglap == 12 or vonglap == 18 or vonglap == 24 or vonglap == 30:
        color = 'pink'
    elif vonglap == 1 or vonglap == 7 or vonglap == 13 or vonglap == 19 or vonglap == 25 or vonglap == 31:
        color = 'blue'
    elif vonglap == 2 or vonglap == 8 or vonglap == 14 or vonglap == 20 or vonglap == 26 or vonglap == 32:
        color = 'green'
    elif vonglap == 3 or vonglap == 9 or vonglap == 15 or vonglap == 21 or vonglap == 27 or vonglap == 33:
        color = 'yellow'
    elif vonglap == 4 or vonglap == 10 or vonglap == 16 or vonglap == 22 or vonglap == 28 or vonglap == 34:
        color = 'orange'
    elif vonglap == 5 or vonglap == 11 or vonglap == 17 or vonglap == 23 or vonglap == 29 or vonglap == 35:
        color = 'red'
    cb.pencolor(str(color))
    vonglap += 1
    while count < 2:
        count += 1
        cb.circle(50,90)
        cb.circle(25,90)
    cb.rt(10)
    count = 0







turtle.done()