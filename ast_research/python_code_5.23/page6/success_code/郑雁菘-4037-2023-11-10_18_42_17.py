A = int(input())
spring = {3,4,5}
summer = {6,7,8}
autumn = {9,10,11}
winter = {12,1,2}
if A in spring:
    print("spring")
elif A in summer:
    print("summer")
elif A in autumn:
    print("autumn")
elif A in winter:
    print("winter")
elif A < 1 or A > 12:
    print("error")
