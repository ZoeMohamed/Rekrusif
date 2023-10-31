def pembagian(x,y):
    if x < y:
        return 0
    else:
        return 1 + pembagian(x-y,y)
  # 12 - 5 = 7 ---> bisa dibagi maka plus 1
  # 7 - 5 == 2 -> bisa dibagi maka plus 1
  # 2-5 = -3 ---> ini gak bisa dibagi maka plus 0
  # 1 + pembagian(7,5) + 1 +pembagian(2,5) + 0

print(pembagian(12,5))