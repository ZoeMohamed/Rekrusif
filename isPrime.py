# # def isPrime(n):
# #     if n > 1:
# #       for i in range(2,n):
# #           if (n % i) == 0:
# #               print(i)
# #               return False
# #       else:
# #               return True
# #     else:
# #         return False
        
# # print(isPrime(2))

# def prime(n):
#     if n == 1:
#         return 1
#     else:
       
#         return n + prime(n - 1)
    
# print(prime(3))





def prime_checker(n,i):
    if n == 1:
      return False

    elif n == i:
        return True
    elif n % i == 0:
         return False
    
    return prime_checker(n,i+1)
        
def prime_number(n):
      return prime_checker(n,2)


print(prime_number(11))
    