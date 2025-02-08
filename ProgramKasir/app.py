print("=========================")
print("     KASIR SEDERHANA     ")
print("=========================")

nama = input("Nama Pelanggan : ")
print(f"Halo {nama}!")
tanggal = (input("Tanggal Pembelian : "))
print("==============================")
print("   ----MENU----   ")
print("1. Ice Tea              Rp.6000")
print("2. Ice Jeruk            Rp.7000")
print("3. Ice Angggur          Rp.7000")
print("4. Jus Alpukat          Rp.8500")
print("5. Air Mineral          Rp.3000")
print("6. Ice Teh              Rp.4000")
print("7. Kopi P/D             Rp.5500")
print("8. Amer                 Rp.9500")
print("9. Vodka                Rp.6000")
print("==============================")
h = []
a = 1

menu_pesanan = int(input("Masukkan menu pesanan lu (Nomor Menu) : "))
if menu_pesanan == 1:
    harga = 6000
elif menu_pesanan == 2:
    harga = 7000
elif menu_pesanan == 3:
    harga = 7000
elif menu_pesanan == 4:
    harga = 8500
elif menu_pesanan == 5:
    harga = 3000
elif menu_pesanan == 6:
    harga = 4000
elif menu_pesanan == 7:
    harga = 5500
elif menu_pesanan == 8:
    harga = 9500
elif menu_pesanan == 9:
    harga = 6000
else:
    while True :
        print("  ----Gada menu itu sowry yea----  ")
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4 or menu_pesanan == 5 or menu_pesanan == 6 or menu_pesanan == 7 or menu_pesanan == 8 or menu_pesanan == 9 or menu_pesanan:
            if menu_pesanan == 1:
                harga = 6000
            elif menu_pesanan == 2:
                harga = 7000
            elif menu_pesanan == 3:
                harga = 7000
            elif menu_pesanan == 4:
                harga = 8500
            elif menu_pesanan == 5:
                harga = 3000
            elif menu_pesanan == 6:
                harga = 4000
            elif menu_pesanan == 7:
                harga = 5500
            elif menu_pesanan == 8:
                harga = 9500
            elif menu_pesanan == 9:
                harga = 6000
                break
            
jumlah_pembelian = int(input("Masukkan jumlah pesanan : "))
for i in range (jumlah_pembelian):
    h.append(harga)
    
while True:
    jawab = input("Apakah ada yang ingin ditambahkan/dikurangi ? (tambah/kurang/tidak) : ")
    if jawab == 'tambah':
        tambah = int(input("Masukkan menu pesanan (Nomor Menu) : "))
        if tambah == 1:
            harga = 6000
        elif tambah == 2:
            harga = 7000
        elif tambah == 3:
            harga = 7000
        elif tambah == 4:
            harga = 8500
        elif tambah == 5:
            harga = 3000
        elif tambah == 6:
            harga = 4000
        elif tambah == 7:
            harga = 5500
        elif tambah == 8:
            harga = 9500
        elif tambah == 9:
            harga = 6000
        jumlah_tambahan = int(input("Masukkan jumlah Pembelian : "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c = jumlah_tambahan + jumlah_pembelian
        print(f"Total pesanan : {c}")
        bayar = sum(h)
        print("Total pembayaran : Rp{}".format(bayar))
        break
    elif jawab == 'kurang':
        kurang = int(input("Berapa jumlah yang dikurangkan? : "))
        for i in range(kurang):
            if h: 
                del h[-1]  
        c = len(h)  
        print("Total pemesanan: ", c)
        bayar = sum(h)
        print("Total Pembayaran : Rp{}".format(bayar))
    else:
        bayar = sum(h)
        c = len(h)  
        print("Total Pemesanan : {}".format(c))
        print("Total Pembayaran : Rp{}".format(bayar))
        break

