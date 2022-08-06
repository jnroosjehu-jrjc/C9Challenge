#coding : UTF-8

non = input("Antre non ou : ")

non22 = non.split()

non23 = []
for n in non22:
    non23.append(n.capitalize())

n = " ".join(non23)

print(n)
