a = int(input("Nhập vào một số nguyên dương a = "))
if(a<=0):
    print("\nSô nhập vào không phải số nguyên dương!\n Hãy nhập lại!")
def giaithua(a):
    t = 1
    if (a == 1):
        return t
    else:
        for i in range(2, a+1):
            t = t * i
        return t
print("Vậy",a,"! = ", giaithua(a))