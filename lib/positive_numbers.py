#function to check true or false

def pos_num(a,b,c):
    if a>0 and b>0 and c>0:
        return False
    elif (a>0 and b>0 and c<0) or (c>0 and a>0 and b<0) or (b>0 and c>0 and a<0):
        return True
    else:
        return False
num = pos_num(1,-3,-2)
print(num)