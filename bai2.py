A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
#phần a
C = list(set(A) & set(B))
print("Các phần tử trùng nhau của hai list A và B được lưu vào list \n C = ", C)
#phần b
A = list(set(A) - set(C))
B = list(set(B) - set(C))
print("Hai list A và B sau khi xóa những phần tử trùng nhau là :\n")
print("A =",A)
print("B =",B)