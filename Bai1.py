A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
#Bài 1 phần a.
B = []
for i in range(0,len(A),1):
        if(A[i]<30):
            B.append(A[i])
print("Các số nhỏ hơn 30 được lưu vào list \n B = ", B)
#Bài 1 phần b.
a = int(input("\nNhập vào một số a = "))
print("\nCác số lớn hơn a trong list là :" )
for i in range(0,len(A),1):
        if(A[i]>a):
            print(A[i])