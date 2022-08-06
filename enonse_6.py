#coding : UTF-8


chn = "Ayibobo Ayiti" 
# "itiyAobobiyA"

ls1 = chn.split()
ls2 = list()
for e in ls1:
    for f in e:
        ls2.append(f)

ls2.reverse()

chn2 = "".join(ls2)
