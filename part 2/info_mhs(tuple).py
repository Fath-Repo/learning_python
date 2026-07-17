list_data_mhs = []
jumlah_mhs = int(input("Jumlah Mahasiswa: "))

for i in range(jumlah_mhs):
    nama_mhs = input("Nama mahasiswa: ")
    nim_mhs = input("NIM: ")
    jurusan_mhs = input("Jurusan: ")

    data_mhs = (nama_mhs, nim_mhs, jurusan_mhs)
    list_data_mhs.append(data_mhs)


i=1
for nama, nim, jurusan in list_data_mhs:
    print(f"===== Data Mahasiswa Ke-{i} =====")
    print(f"Nama mahasiswa: {nama}")
    print(f"NIM: {nim}")
    print(f"Jurusan: {jurusan}")
    i+=1