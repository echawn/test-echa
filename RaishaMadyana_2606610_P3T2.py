#   buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

#   buah[2] = "cherry"
#   buahuser = input("Masukkan Nama Buah yang di inginkan: ")
#   induser = int(input("pada index berapa buah ingin dimasukkan? "))
#   buah.insert(induser, buahuser)
#   list dapat memuat lebih dari satu tipe data
#   buah.sort()
#   print(buah)

#data jumlah produk yang terjual selama lima hari
#hari pertama 120, hari kedua 150, ketiga 135 , keempat 180, kelima 160
#mengecek ulang 1-5, kesalahan di hari ketiga, harusnya 140 produk yang terjual
#saya ingin menmbahkan hari keenam, produk terjual 175
#ada kesalahan kembali, hari ketiga seharusnya adalah 155
#menghitung laba, hari kedua tidak dihitung
#menghitung, total produk yang terjual, pendapatan kotor, biaya platform 5%, pendapatan bersih, penjualan tertinggi, terendah, selisih penjualan tertinggi dan terendah

#RAISHA MADYANA 2606610

data_penjualanH1 = int(input("jumlah penjualan hari ke 1: "))
data_penjualanH2 = int(input("jumlah penjualan hari ke 2: "))
data_penjualanH3 = int(input("jumlah penjualan hari ke 3: "))
data_penjualanH4 = int(input("jumlah penjualan hari ke 4: "))
data_penjualanH5 = int(input("jumlah penjualan hari ke 5: "))

data_penjualan = [data_penjualanH1, data_penjualanH2, data_penjualanH3, data_penjualanH4, data_penjualanH5]

indperbaikan1 = int(input("Perbaikan pada hari ke: "))
varperbaikan1 = int(input("Jumlah penjualan = "))

data_penjualan [indperbaikan1-1] = varperbaikan1

data_penjualanH6 = int(input("jumlah penjualan hari ke 6: "))
data_penjualan.append(data_penjualanH6)

indperbaikan2 = int(input("Perbaikan pada hari ke (dimulai dari 0): "))
varperbaikan2 = int(input("Jumlah penjualan = "))

data_penjualan.insert(indperbaikan2, varperbaikan2)
data_penjualan.pop(1)

data_penjualan [indperbaikan2-1] = varperbaikan2
print(data_penjualan)
total_pjual = sum(data_penjualan)
pendapatan_kotor = total_pjual*75000
biaya_platform = pendapatan_kotor*(5/100)
pendapatan_bersih = pendapatan_kotor-biaya_platform
jual_tinggi = min(data_penjualan)
jual_rendah = max(data_penjualan)
jual_selisih = jual_tinggi - jual_rendah

print("Total Produk terjual : ", total_pjual)
print("Pendapatan kotor: ", pendapatan_kotor)
print("Biaya platform: ", biaya_platform)
print("pendapatan bersih: ", pendapatan_bersih)
print("Penjualan Tertinggi: ", jual_tinggi)
print("Penjualan Terendah: ", jual_rendah)
print("Selisih penjualan tertinggi dan terendah: ", jual_selisih)



