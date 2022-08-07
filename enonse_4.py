#coding : UTF-8
#thk_2_rtchy

enf = 1
sip = 20


num, num1 = 2, 3


sum = sum1 = sum2 = sum3 = 0

print("------------------------------------------")
print(f"Lis nonb miltipl {num} men miltipl {num1} \n")
for i in range(enf, sip):
    if (i%num)==0 and(i%num1)!=0:
        sum = sum + 1
        print(i, end=" ")
print(f" | Total :   {sum}")

print("------------------------------------------")
print(f"Lis nonb miltipl {num1} /pa miltipl {num} \n")
for i in range(enf,sip):
    if (i%num)!=0 and (i%num1)==0:
        sum1 = sum1 + 1
        print(i, end=" ")
print(f" | Total : {sum1}")


print("------------------------------------------")
print(f"Lis nonb miltipl {num} / miltipl {num1} \n")  
for i in range(enf,sip):
    if (i%num)==0 and (i%num1)==0:
        sum2 = sum2 + 1
        print(i, end=" ")
print(f" | Total :  {sum2}")


print("------------------------------------------")
print(f"Lis nonb ki pa miltipl {num} e ki pa miltipl {num1} \n")
for i in range(enf,sip):
    if (i%num)!=0 and (i%num1)!=0:
        sum3 = sum3 + 1
        print(i, end=" ")
print(f" | Total : {sum3}")
