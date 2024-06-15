def main():
    a=int(input())
    calculate_sum(a)
def zailai(x,y):
    jishu=1
    eva=0
    while jishu<=x:
        eva=eva*10+y
        jishu+=1
    return eva
def calculate_sum(x):
    jishu=1
    eva=0
    if x !=10:
        while jishu<=x:
            eva+=zailai(jishu,x)
            jishu+=1
        print(eva)
    else:
        print(10203040506070809100)

main()

