#program pemesanan tiket
harga_reguler = 50000
harga_vip = 100000

diskon_member = 0.2

tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

if tipe_tiket == "reguler":
    harga = harga_reguler
elif tipe_tiket == "vip":
    harga = harga_vip
else:
    harga = 0
    print("Tipe tiket tidak valid!")

if harga != 0:
    harga_akhir = harga * (1 - diskon_member) if status_member == "ya" else harga
    print("Total harga yang harus dibayar: Rp", int(harga_akhir))
