def kali(x,y):
    if y == 0:
        return 0
    
    else:
        return x + kali(x,y-1)
    # 2 + kali(2,2) + 2  + kali(2,1) + 2 + kali(2,0) + 0

def kalirekx(x,y):
    if x == 0:
        return 0
    else:
        return y + kali(x-1,y)
    # 3 + kalirekx(1,3) + 3 + kalirekx(0,3) + 0 
print(kali(2,3))