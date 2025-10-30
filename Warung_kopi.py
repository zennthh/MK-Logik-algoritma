harga_kopi = 15000
harga_sandwich = 25000
harga_kentang = 20000

kopi = int(input("Masukan jumlah kopi: "))
sandwich = int(input("Masukan jumlah sandwich: "))
kentang = int(input("Masukan jumlah kentang: "))
uang = int(input("Masukan jumlah uang yang di bayarkan: "))
total = (harga_kopi * kopi) + (harga_sandwich * sandwich) + (harga_kentang * sandwich)
kembalian = uang - total 
print()
print ("=== Selamat datang di warung kopi ceria ====")
print ("Daftar harga:")
print (f"Kopi : Rp. {harga_kopi}/gelas")
print (f"sandwich : Rp. {harga_sandwich}/porsi")
print (f"kentang: Rp. {harga_kentang}/porsi")
print()
print("Rincian pembelian:")
print (f"Kopi: {kopi} gelas")
print (f"sandwich {sandwich} porsi")
print (f"kentang {kentang} porsi")
print()
print (f"Tota harga: {total}")
print (f"Uang yang di bayarkan: {uang}")
print ("apakah uang mu cukup? True" if uang >= total else "apakah uang mu cukup? false")
print (f"kembalianmu: {kembalian}" if uang >= total else "Kembalianmu: 0")

