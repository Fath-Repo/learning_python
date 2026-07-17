jumlah_mhs = int(input("Berapa jumlah mahasiswa: "))
list_nilai_mhs =[]
total_nilai = 0
nilai_tertinggi = 0
nilai_terendah = 100
a_counter = 0
b_counter = 0
c_counter = 0
d_counter = 0
e_counter = 0
lulus_counter = 0
tdklulus_counter = 0
print()

for i in range(jumlah_mhs):
    nama_mhs = input("Nama mahasiswa\t: ")
    nilai_mhs = int(input(f"Nilai mahasiswa\t: "))
    if nilai_mhs > 100 or nilai_mhs < 0:
        print("Invalid input. Mohon lakukan input ulang")
        break
    elif 85 <= nilai_mhs:
        grade_mhs = "A"
        a_counter+=1
    elif 75 <= nilai_mhs < 85:
        grade_mhs = "B"
        b_counter+=1
    elif 55 <= nilai_mhs < 75:
        grade_mhs = "C"
        c_counter+=1
    elif 40 <= nilai_mhs < 55:
        grade_mhs = "D"
        d_counter+=1
    else:
        grade_mhs = "E"
        e_counter+=1
    
    if grade_mhs in ("A", "B", "C"):
        status_mhs = "Lulus"
        lulus_counter+=1
    else:
        status_mhs = "Tidak Lulus"
        tdklulus_counter+=1
    
    data_mhs = (nama_mhs, nilai_mhs, grade_mhs, status_mhs)
    list_nilai_mhs.append(data_mhs)

    total_nilai += nilai_mhs

    if nilai_mhs > nilai_tertinggi:
        nilai_tertinggi = nilai_mhs
    
    if nilai_mhs < nilai_terendah:
        nilai_terendah = nilai_mhs

print()
counter = 1
for nama, nilai, grade, status in list_nilai_mhs:
    print(f"===== Data mahasiswa ke-{counter} =====")
    print(f"Nama\t: {nama}")
    print(f"Nilai\t: {nilai}")
    print(f"Grade\t: {grade}")
    print(f"Status\t: {status}")
    counter+=1

print()
print("===== Rangkuman data nilai mahasiswa =====")
print(f"Nilai tertinggi\t\t\t: {nilai_tertinggi}")
print(f"Nilai terendah\t\t\t: {nilai_terendah}")
print(f"Jumlah mahasiswa lulus\t\t: {lulus_counter}")
print(f"Jumlah mahasiswa tidak lulus\t: {tdklulus_counter}")
print(f"Rata rata\t\t\t: {total_nilai/jumlah_mhs}")
print(f"Jumlah mahasiswa dengan grade A\t: {a_counter}")
print(f"Jumlah mahasiswa dengan grade B\t: {b_counter}")
print(f"Jumlah mahasiswa dengan grade C\t: {c_counter}")
print(f"Jumlah mahasiswa dengan grade D\t: {d_counter}")
print(f"Jumlah mahasiswa dengan grade E\t: {e_counter}")





