def cal(a,v):
    x=v**2/(2*a)
    return x
n=str(input())
a=eval(input())
v=eval(input())
print(f"The acceleration of {n} is {'%.2f'%a} M / s, the take-off speed is {'%.2f'%v} M / s, and the shortest take-off runway length is {'%.2f'%cal(a,v)} M.")

