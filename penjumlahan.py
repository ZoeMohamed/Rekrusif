def penjumlahan(x,y):
    if y == 0:
        return x
    else:
        return  penjumlahan(x,y-1) + 1
    # 1 + penjumlahan(1,0) + 0
    # 4 + penjumlahan(2,3) + 
# penjumlahan(2,1) + 1 + penjumlahan(2,0) + 1 + 2
print(penjumlahan(2,2))

def penjumlahanrekx(x,y):
    if x == 0:
        return y
    else:
        return penjumlahanrekx(x-1,y) + 1
print(penjumlahanrekx(2,9))