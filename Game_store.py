print()
harga = 2000
jumlah_diamond = int(input("Masukan jumlah diamond yang ingin di beli: "))
uang = int(input("Masukan uang nya:"))
total = jumlah_diamond * harga
kembalian = uang - total
print()
print ("<===== Selamat Datang di Game Store: =====>")
print () 
print (f"Jumlah diamond yang di beli: {jumlah_diamond}")
print (f"Total bayar: {total}")
print (f"Uang yang dibayarkan: {uang}")
print ("apakah uang mu cukup? True" if uang >= total else "apakah uang mu cukup? False")
print (f"Kembalianmu: {kembalian}" if uang >= total else "kembalianmu: 0")



