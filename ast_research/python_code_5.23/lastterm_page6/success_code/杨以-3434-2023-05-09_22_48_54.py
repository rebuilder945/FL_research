p1=input()
p2=input()
r="red"
b="blue"
y="yellow"
if {p1,p2}=={r,b}:
    print('purple')
if {p1,p2}=={r,y}:
    print('orange')
if {p1,p2}=={y,b}:
    print('green')
if {p1,p2}!={r,b} and  {p1,p2}!={r,y} and {p1,p2}!={b,y}:
    print('error')

