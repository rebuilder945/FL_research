import turtle as t,random
t.penup()
t.fd(-300)
t.pendown()
t.circle(-20,15)
colorlist=["red","orange","yellow","green","blue","purple"]
t.color("red")
t.pensize(20)
for i in range(5):
    t.color(random.choice(colorlist))
    t.circle(50,60)
    t.circle(-60,60)
t.color("blue")
t.circle(-50,30)
t.color("green")
t.circle(-50,120)
t.color("yellow")
t.fd(70)
t.done()
