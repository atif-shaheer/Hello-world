from turtle import*

speed(0)

title("b'day cake")
bgcolor("skyblue")


up()
goto(-90,-50)

color("red")

begin_fill()
for i in range(1):
    down()
    pencolor("black")
    pensize(2)
    fd(180)
    left(90)
    fd(120)
    left(90)
    fd(180)
    left(90)
    fd(120)
    continue
end_fill()

color("silver")

begin_fill()
for j in range(1):
    pencolor("black")
    pensize(2)
    right(90)
    fd(30)
    left(90)
    fd(20)
    left(90)
    fd(240)
    left(90)
    fd(20)
    left(90)
    fd(210)
    continue
end_fill()

right(90)
fd(120)
right(90)
fd(40)

color("yellow")
begin_fill()
for k in range(1):
    pencolor("black")
    pensize(2)
    left(90)
    fd(70)
    right(90)
    fd(100)
    right(90)
    fd(70)
    right(90)
    fd(100)
end_fill()

right(90)
fd(70)
right(90)
fd(45)

color("white")
begin_fill()
for l in range(1):
    pencolor("black")
    pensize(2)
    left(90)
    fd(30)
    right(90)
    fd(10)
    right(90)
    fd(30)
    right(90)
    fd(10)
end_fill()

right(90)
fd(30)
right(90)
fd(5)

color("orange")

begin_fill()
for m in range(1):
    pencolor("black")
    pensize(1)
    circle(5,360)
end_fill()

up()
goto(0,0)
down()
write("Happy b'day")

up()
goto(-250,150)

color = ['blue', 'green']

for n in range(2):
    down()
    pencolor("black")
    pensize(2)
    begin_fill()
    fillcolor(color[n])
    circle(30,360)
    end_fill()
    circle(-5)
    right(90)
    fd(200)
    up()
    home()
    bk(150)

up()
goto(250,150)

color = ['red', 'yellow']

for o in range(2):
    down()
    pencolor("black")
    pensize(2)
    begin_fill()
    fillcolor(color[o])
    circle(30,360)
    end_fill()
    circle(-5)
    left(90)
    bk(200)
    up()
    home()
    fd(150)
    continue

up()
goto(-100,200)

colors = ['red', 'yellow','green','blue','red', 'yellow','green','blue','red', 'yellow','green','blue','red', 'yellow','green','blue',]

for p in range(8):
    down()
    begin_fill()
    fillcolor(colors[p])
    circle(5)
    left(45)
    end_fill()
    up()
    fd(30)

up()
goto(100,200)

colors = ['red', 'yellow','green','blue','red', 'yellow','green','blue','red', 'yellow','green','blue','red', 'yellow','green','blue',]

for p in range(8):
    down()
    begin_fill()
    fillcolor(colors[p])
    circle(5)
    left(45)
    end_fill()
    up()
    fd(30)
done()
