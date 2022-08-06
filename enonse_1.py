#coding : UTF-8


import ipaddress

def rekipereIp():
    while True:
        try:
            ip = input("Antre yon address ip : ")
            return ipaddress.ip_address(ip)
        except ValueError:
            print("Address ip sa a pa valid ! ")

ip = rekipereIp()
ip = str(ip)

# ip = "127.0.0.1"
ipT  = ip.split(".")    # rekipere chak moso nan ip a nan yon lis 

ipT2 = []   
for e in ipT:
    for i in e:
        ipT2.append(int(i))

s = 0        
for k in ipT2:
    s+=k
pot = s*ipT2[0]


print(f"Pot ki aksesib la se : {pot}")