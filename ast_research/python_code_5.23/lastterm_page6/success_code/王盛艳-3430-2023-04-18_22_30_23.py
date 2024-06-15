s = {"spring":"3,4,5,","summer":"6,7,8","autumn":"9,10,11","winter":"12,1,2"}
m = int(input())
if m in range(3,6):
    print("spring")
if m in range(6,9):
    print("summer")
if m in range(9,12):
    print("autumn")
if m == 12 or m == 1 or m == 2:
    print("winter")
if m not in range(1,13):
    print("error")
