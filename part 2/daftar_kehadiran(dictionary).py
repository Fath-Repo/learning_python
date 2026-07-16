daftar_kehadiran = {}
jumlah_mhs = int(input("Jumlah mahasiswa: "))
hadir_counter = 0
sakit_counter = 0
izin_counter = 0
alpha_counter = 0

for i in range(jumlah_mhs):
    nama_mhs = (input("Nama mahasiswa: "))
    kehadiran = (input("Kehadiran (hadir/sakit/izin/alpha): "))
    if kehadiran.lower() != "hadir" and kehadiran.lower() != "sakit" and kehadiran.lower() != "izin" and kehadiran.lower() != "alpha":
        print("Maaf, kehadiran tidak ada dalam daftar pilihan, harap mengulangi input dari awal")
        break

    daftar_kehadiran.update({nama_mhs:kehadiran})

    if kehadiran.lower() == "hadir":
        hadir_counter+=1
    elif kehadiran.lower() == "sakit":
        sakit_counter+=1
    elif kehadiran.lower() == "izin":
        izin_counter+=1
    else:
        alpha_counter+=1



print()
print("========== Daftar Absensi Mahasiswa ==========")
for key, value in daftar_kehadiran.items():
    print(f"{key} : {value}")

print(f"Jumlah hadir\t: {hadir_counter}")
print(f"Jumlah sakit\t: {sakit_counter}")
print(f"Jumlah izin\t: {izin_counter}")
print(f"Jumlah alpha\t: {alpha_counter}")
