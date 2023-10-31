import math

N = int(input()) 
M = int(input()) 
R = int(input())

def ledakkan_semuanya(a,b,r) :
    min_range = min(abs(a-1), abs(b-1))
    bombs = math.ceil(min_range%r)
    return bombs

print(ledakkan_semuanya (N, M, R))