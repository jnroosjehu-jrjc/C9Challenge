#coding: UTF-8


chn = "hiddenXPeopleendpass"

a = chn.index("hidden")
a = a + len("hidden")
b = chn.index("endpass")


rch = chn[a:b]


print(rch)