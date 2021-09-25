a = int(input("Nhập vào một số nguyên dương a = "))
def tong(a):
    t=0
    while( a > 0):
        t = t + (a%10)
        a = int(a/10)
    return t
print("\nTổng các chữ số của số a đã nhập là :",tong(a) )