nama = input("Masukan nama : ")
for i in range(0,len(nama)):
    for j in range(i):
        print(nama[j], end=(""))
    print()
for i in range(len(nama), 0, -1):
    for j in range(i):
        print(nama[j], end=(""))
    print()