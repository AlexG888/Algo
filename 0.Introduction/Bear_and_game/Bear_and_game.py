q = int(input())
mishka, kris =0,0

for _ in range(q):
  a,b = map(int, input().split())
  if a > b:
    mishka+=1
  elif a < b:
    kris+=1
        
if mishka > kris:
  print('Mishka')
elif mishka < kris:
  print('Chris') 
else:
  print('Friendship is magic!^^')
  
# 3
# 3 5
# 2 1
# 4 2
#
# Mishka