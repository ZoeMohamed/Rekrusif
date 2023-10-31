def pangkat(x,y):
    if y == 0:
        return 1
    else:
        return x * pangkat(x,y-1)
    
    # pemanggilan pertama
    # Masuk Ke else scope karena y == 3
    #  2 * pangkat(2,2)
    
    # Pemanggilan Kedua
    # Masuk ke else scope karena y == 2
    # 2 * pangkat(2,1)

    # Pemanggilan Ketiga
    # Masuk ke else scope karena y == 1
    #  2 * pangkat(2.0)

    # Pemanggilan Keempat
    # masuk ke if pertama y == 0
    # 2*2**2*1

    # 2 * pangkat(2,2) * 2 * pangkat(2,1) * 2 * pangkat(2,0) * 1

    # 2 * pangkat(2,2)
    # pangkat(2,2) berisi 2* pangkat(2,1)
    # pangkat(2,1) berisi 2*pangkat(2,0)
    # pangkat(2,0) berisi 1

print(pangkat(2,1))

