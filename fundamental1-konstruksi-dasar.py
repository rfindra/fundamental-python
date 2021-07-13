# Konstruksi Dasar Python

# Sequential: Eksekusi code secara berurutan
print("Hello World")
print("by Indra Rizky Firmansyah")
print("12 July 2021")
print("-" * 25)

# Percabangan : Eksekusi Terpilih
ingin_cepat = True  # ingin_cepat adalah variabel bernilai "True"
if ingin_cepat:
    print("Jalan Lurus")  # Jika Nilai variable True, maka ini akan di print ke layar
else:
    print("ambil jalan lain")  # Jika nilai variable False, maka ini akan di print ke layar

# Perulangan
jumlah_anak = 4

for urutan_anak in range (1, jumlah_anak+1): # Jumlah perulangan = 5 - 1 = 4 (perhitungan dalam pemrograman di mulai dari 0)
    print(f"Halo anak #{urutan_anak}")

#
