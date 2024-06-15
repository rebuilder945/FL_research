x=eval(input())
def f(x):
    jishu=0
    if x<20:
       jishu=x**x*6+1
    elif x>=20 and x<=40:
        jishu=(3*x-60)**0.5
    elif x>=40:
        jishu=100/(x+1)
    print("%.2f"%jishu) 
