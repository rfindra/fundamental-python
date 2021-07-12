print("\nTipe data sederhana/skalar ")
anak1 = "indra"
anak2 = "rizky"
anak3 = "firmansyah"

print(anak2)

print("\nTipe data list/daftar/array")
anak = ["Indra", "Rizky", "Firmansyah"] # array
print(anak)
anak.append("kafka") # "anak.append" di gunakan untuk menambahkan daftar baru pada array
print(anak)

print("\nSapa anak ke-3")
print(f"Hai {anak[2]}!")

print("\nSapa semua anak")
for a in anak:
    print(f"Hai {a}!")

print("\nSapa semua anak : cara ribet")
for a in range (0, len(anak)): # "len" di gunakan untuk mengambil jumlah dari array/list
    print(f"{a+1}. Hai {anak[a]}")
print("*"*25)


