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

print(gcd(0,2))
# def fpb(x,y):
#     maxima = max(x,y)
#     minima = min(x,y)

#     if y == 9:
#        return minima
#     else:
#        return fpb(max(x,y),minima % maxima)
       
# print(fpb(20,30))
         