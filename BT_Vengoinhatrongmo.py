import turtle
hung_screen = turtle.Screen()
cb = turtle.Turtle()
turtle.bgcolor("LightBlue")

# Vẽ ngôi nhà hình vuông màu xanh dương
cb.fillcolor("Blue")
cb.begin_fill()
cb.fd(50)
cb.lt(90)
cb.fd(50)
cb.lt(90)
cb.fd(50)
cb.lt(90)
cb.fd(50)
cb.lt(90)
cb.end_fill()

# Vẽ, tô màu cửa
cb.fillcolor("LightGreen")
cb.begin_fill()
cb.fd(20)
cb.lt(90)
cb.fd(25)
cb.rt(90)
cb.fd(10)
cb.rt(90)
cb.fd(25)
cb.end_fill()

# Di chuyển đến vị trí góc phải bên trên của ngôi nhà (cb.penup();cb.goto(50,50);cb.pendown())
cb.lt(90)
cb.fd(20)
cb.lt(90)
cb.fd(50)

# Vẽ nóc đằng trước hình tam giác màu hồng
cb.fillcolor("Pink")
cb.begin_fill()
cb.lt(60)
cb.fd(29)
cb.lt(60)
cb.fd(29)
cb.end_fill()

cb.backward(29)
cb.lt(160)

# Vẽ phía sau của nóc màu cam
cb.fillcolor("orange")
cb.begin_fill()
cb.fd(28)
cb.rt(40)
cb.fd(29)
cb.rt(140)
cb.fd(28)
cb.end_fill()
cb.lt(80)

# Vẽ mặt tường còn lại của ngôi nhà
cb.fillcolor("Yellow")
cb.begin_fill()
cb.fd(50)
cb.lt(102)
cb.fd(29.5)
cb.lt(80)
cb.fd(47.5)
cb.lt(95)
cb.fd(28)
cb.end_fill()

cb.penup()
cb.home()
cb.goto(59.5,25)
cb.pendown()

# Vẽ khung cửa sổ màu nâu cho ngôi nhà
cb.fillcolor("brown")
cb.begin_fill()
cb.lt(12)
cb.fd(9.5)
cb.lt(78)
cb.fd(9.5)
cb.lt(102)
cb.fd(9.5)
cb.lt(78)
cb.fd(9.5)
cb.end_fill()

cb.penup()
cb.home()
cb.goto(125,-5)
cb.pendown()

# Vẽ thân cây
cb.fillcolor("Brown")
cb.begin_fill()
cb.fd(12)
cb.lt(90)
cb.fd(25)
cb.lt(90)
cb.fd(12)
cb.lt(90)
cb.fd(25)
cb.end_fill()

# Vẽ lá cây
cb.backward(25)
cb.rt(90)
cb.fillcolor("Green")
cb.begin_fill()
cb.fd(22)
cb.rt(135)
cb.fd(39.5)
cb.rt(90)
cb.fd(39.5)
cb.rt(135)
cb.fd(22)
cb.end_fill()

cb.penup()
cb.fd(6)
cb.rt(90)
cb.fd(28)
cb.lt(90)
cb.pendown()

# Phần giữa
cb.fillcolor("Green")
cb.begin_fill()
cb.fd(24)
cb.rt(135)
cb.fd(33.9)
cb.rt(90)
cb.fd(33.9)
cb.rt(135)
cb.fd(24)
cb.end_fill()

cb.penup()
cb.rt(90)
cb.fd(24)
cb.lt(90)
cb.pendown()

# Ngọn cây
cb.fillcolor("Green")
cb.begin_fill()
cb.fd(20)
cb.rt(135)
cb.fd(28.2)
cb.rt(90)
cb.fd(28.2)
cb.rt(135)
cb.fd(20)
cb.end_fill()

cb.penup()
cb.home()


turtle.Turtle()
turtle.penup()
turtle.goto(100, 150)
turtle.pendown()
turtle.fillcolor ("yellow")
turtle.begin_fill()
turtle.circle (20)
turtle.end_fill()

cb.pensize(5)
cb.pencolor("orange")
cb.speed(10)
cb.goto(100,150)
cb.rt(90)
cb.fd(10)
cb.pendown()
cb.fd(20)
cb.penup()
cb.goto(150,170)
cb.pendown()
cb.rt(90)
cb.fd(20)
cb.penup()
cb.goto(100,205)
cb.pendown()
cb.rt(90)
cb.fd(20)
cb.penup()
cb.goto(65,170)
cb.pendown()
cb.lt(90)
cb.fd(20)
cb.penup()
cb.goto(75,150)
cb.pendown()
cb.lt(45)
cb.fd(10)
cb.penup()
cb.backward(72)
cb.pendown()
cb.lt(180)
cb.fd(10)
cb.penup()
cb.goto(120,150)
cb.pendown()
cb.rt(90)
cb.fd(10)
cb.penup()
cb.backward(72)
cb.pendown()
cb.lt(180)
cb.fd(20)































turtle.done()