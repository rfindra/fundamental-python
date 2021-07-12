"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {"anak": "son", "istri": "wife", "ayah": "father"}
"""
kamus_ind_eng = {}
kamus_ind_eng["anak"] = "son"
kamus_ind_eng["istri"] = "wife"
kamus_ind_eng["ayah"] = "father"
"""
print(kamus_ind_eng)
print(kamus_ind_eng["ayah"])
print('\n')
print("Data ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi")
data_dari_server_gojek = {
    "tanggal":"2021-07-13",
    "driver_list":["indra","rizky","firmansyah"]
}

# print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list'][2]}")

print("Data ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi")
data_dari_server_gojek = {
    "tanggal":"2021-07-13",
    "driver_list":[{"nama": "indra","jarak": 10},
                   {"nama":"rizky", "jarak":15},
                   {"nama": "firmansyah", "jarak":100}
                   ]
}

#print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"\nDriver #2 {data_dari_server_gojek['driver_list'][2]}")
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']}meter")