import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i ==0:
            return False
    return True
result=0
for x in range (2 , 100):
    if (is_prime(x)):
        result+=x
print(result)