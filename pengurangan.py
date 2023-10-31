def pengurangan(x,y):
    if x == 0:
        return y
    else:
        return pengurangan(x-1,y) - 1
    
    # pengurangan(1,9) -  1 - pengurangan(0,9) - 1 

print(pengurangan(2,9))


def penguranganreky(x,y):
    if y == 0:
        return x
    else:
        return penguranganreky(x,y-1) - 1
    # pengurangan(3,1) - 1 
    # pengurangan(3,0) - 1
    # 3

print(penguranganreky(3,2))