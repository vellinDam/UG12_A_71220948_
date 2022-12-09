Batas=int(input("masukkan pembatas : "))
Larang=int(input("masukkan angka yang dilarang : "))

for i in range(Batas):
    if(i==Larang):
        continue
    else:
        print(i,end=" ")