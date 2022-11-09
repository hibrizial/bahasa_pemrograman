def penjualan():
    c = "capuccino"
    t = "teh"
    print ("pilihan")
    print ("1.", c)
    print ("2.", t)
    print ("3.", exit)

def welcome():
    nim = (input("NIM : "))
    nama = (input("Nama : "))

def capuccino():
    c = "memilih capuccino"
    print (c)
    harga = int(input("Masukan Harga : "))
    bayar = harga + (harga * 10/ 100)
    print ("Jumlah yang harus dibayar : ", bayar)

def teh():
    c = "memilih teh"
    print (c)
    harga = int(input("Masukan Harga : "))
    bayar = harga + (harga * 10/ 100)
    print ("Jumlah yang harus dibayar : ", bayar)

while True:
    welcome()
    penjualan()
    choice = int(input("Masukan Pilihan : "))
    if choice == 1:
        capuccino()
    elif choice == 2:
        teh()
    elif choice == 3:
        break
    else:
        print ("pilihan salah")