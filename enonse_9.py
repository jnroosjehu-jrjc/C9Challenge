#coding : UTF-8

a = 5
b = 20

ls = [x for x in range(a, b+1)]


t = 0
for i in ls:
    if i%2==0:
        t+=i
        
        

print(f" Total : {t}")