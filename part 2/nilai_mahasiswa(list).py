jumlah_mhs = int(input("Berapa jumlah mahasiswa: "))
list_nilai_mhs =[]
total_nilai = 0
nilai_tertinggi = 0
nilai_terendah = 100
print()

for i in range(jumlah_mhs):
    nilai_mhs = int(input(f"Nilai mahasiswa {i+1}\t: "))
    if nilai_mhs > 100 or nilai_mhs < 0:
        print("Invalid input. Mohon lakukan input ulang")

    total_nilai += nilai_mhs
    list_nilai_mhs.append(nilai_mhs)

    if nilai_mhs > nilai_tertinggi:
        nilai_tertinggi = nilai_mhs
    
    if nilai_mhs < nilai_terendah:
        nilai_terendah = nilai_mhs

print()
counter = 0
print("Data nilai: ")
for nilai in list_nilai_mhs:
    print(f"Nilai mahasiswa {counter+1}: {nilai}")
    counter+=1

print()
print(f"Nilai tertinggi\t: {nilai_tertinggi}")
print(f"Nilai terendah\t: {nilai_terendah}")
print(f"Rata rata\t: {total_nilai/jumlah_mhs}")



