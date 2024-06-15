def main():
    num = eval(input())
    calculate_e(num)
def jiecheng(x):
    z=1
    w=1
    while z<=x:
        w*=z
        z=z+1
    return w

def calculate_e(x):
    eva=1
    jishu=1
    while x>0:
        eva+=1/jiecheng(jishu)
        jishu+=1
        x-=1
    print("%.6f"%eva)
main()


