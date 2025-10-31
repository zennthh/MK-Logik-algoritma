def hitung_harga_tiket():
    harga = {
        "biasa": {"non_member": 60000, "member": 45000},
        "hari_pekan": {"non_member": 90000, "member": 70000}
    }

    while True: 
        hari = input("Masukan hari konser: (biasa/hari_pekan): ").lower().strip()
        if hari in ["biasa", "hari_pekan"]:
            break
        else:
            print("Input tidak valid")

    while True:
        status = input("Masukan status pembeli (member, non_member): ").lower().strip()
        if status in ["member", "non_member"]:
            break
        else:
            print("Input tidak valid")

    while True:
        try:
            jumlah = int(input("Masukan jumlah tiket: "))
            if jumlah > 0:
                break
            else:
                print("Input tidak valid")
        except ValueError:
            print("Input tidak valid, masukkan angka positif")

    harga_pertiket = harga[hari][status]
    total_harga = harga_pertiket * jumlah

    if jumlah > 3:
        diskon = total_harga * 0.10
        total_harga -= diskon

    print(f"Hari yang dipilih: {hari}")
    print(f"Status pembeli: {status}")
    print(f"Jumlah tiket: {jumlah}")
    print(f"Total harga setelah diskon: Rp.{total_harga:.0f}")

    print ("=== Silahkan melakukan pembayaran ===")
    print()
    
    while True:
        uang_pengunjung = int(input("Silahkan masukan nomimal:" ))
        if uang_pengunjung >= total_harga:
            print ("Pembayaran berhasil")
            break
        else:
            print ("Maaf uang tidak cukup")
            
hitung_harga_tiket()


