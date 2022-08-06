#coding : UTF-8

chn = "5 45 123  12"
# ap bay (5) * (4+5) * (1+2+3) * (1+2) => 5*9*6*3
# ki bay total: 810

chn = "50 45 123  12"

chn2 = chn.split()
chn3 = []
for x in chn2:
    chn3.append(list(x))

v = list()
for e in chn3:
    for f in e:
        s = 0
        s+=int(f)
        v.append(s)
    

print(v)

