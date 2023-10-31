x = 30
y = 40
fpb = 0
for i in range(1,max(x,y)):
    if x % i == 0 and y % i == 0:
      fpb = i
  # print(i)
# print(fpb)
def gcd(a, b): 
    if b == 0: 
        return a 
    else: 
        return gcd(b, a % b) 
    
# gcd (30,20)
# gcd(20,10)
# gcd(10,0)
# b == 0
# maka A yaitu 10 


# gcd(2,4)
# gcd(4,2)
# gcd(2,4 % 2 )
# gcd(2,0)
# b == 0
# maka hasilnya A yaitu 2

# print(gcd(10,30))
print(2%4)
# def fpb(x,y):
#     maxima = max(x,y)
#     minima = min(x,y)

#     if y == 9:
#        return minima
#     else:
#        return fpb(max(x,y),minima % maxima)
       
# print(fpb(20,30))
         