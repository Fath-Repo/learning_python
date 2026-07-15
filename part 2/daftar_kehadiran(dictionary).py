daftar_kehadiran = {
    "Andi":"Hadir",
    "Budi":"Alpha",
    "Citra":"Hadir",
    "Dina":"Izin"
}
hadir_counter = 0
sakit_counter = 0
izin_counter = 0
alpha_counter = 0

for nama,kehadiran in daftar_kehadiran.items():
    print(f"Nama Mahasiswa\t: {nama}")
    print(f"Kehadiran\t: {kehadiran}")
    if kehadiran.lower() == "hadir":
        hadir_counter+=1
    elif kehadiran.lower() == "sakit":
        sakit_counter+=1
    elif kehadiran.lower() == "izin":
        izin_counter+=1
    elif kehadiran.lower() == "alpha":
        alpha_counter+=1

print(f"Jumlah hadir\t: {hadir_counter}")
print(f"Jumlah sakit\t: {sakit_counter}")
print(f"Jumlah izin\t: {izin_counter}")
print(f"Jumlah alpha\t: {alpha_counter}")
