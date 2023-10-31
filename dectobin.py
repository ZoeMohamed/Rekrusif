def decimaltobinary(x):
    if x == 0:
      return ""
    else:
      return    decimaltobinary(x//2) + str(x%2)
    # 1 + 10 * 0

print(decimaltobinary(128))
print(1%2)
# 8//2 -> 4
# 4//2 -> 2
# 2//2 -> 1
# 1//2 ->
       