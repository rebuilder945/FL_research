import math
def sushu(m):
    if m<=1:
        return False
    for i in range(2,int(math.sqrt(m)+1)):
        if m%1==0:
            return False
    return True
