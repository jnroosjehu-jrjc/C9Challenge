#coding : UTF-8



tab = [17, 0, 2, -5, 500]

M = tab[0] #pi gwo nonb
m = tab[0] #pi piti nonb

for i in range(len(tab)):
    if tab[i] > M:
        M = tab[i]
    if tab[i]<i:
        m = tab[i]
        
        
print("Pi gwo nonb :", M)
print("Pi piti nonb :", m)
