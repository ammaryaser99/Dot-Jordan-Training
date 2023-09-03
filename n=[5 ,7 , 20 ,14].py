n=[5 ,7 , 20 ,14]
max=0
max_2=0
for i in range(1,len(n)):
    if n[i]>max:
        max_2=max
        max=n[i]
    elif n[i]>max_2:
        max_2=n[i]
print(max_2)