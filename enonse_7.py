#coding : UTF-8

v = "aeiouyAEIOUY"

txt = "ALE TOUNEN VINI"

for i in range(len(txt)) :
    if txt[i] in v:
        txt = txt.replace(txt[i-1],"*")
print(txt)