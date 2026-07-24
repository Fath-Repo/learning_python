list_students = []

print("===== Sistem Pengelolaan Nilai Mahasiswa =====")

#Input
while True:
    data_student = dict()
    nama_mahasiswa = input("Nama mahasiswa: ").strip().lower()
    nim_mahasiswa = input("NIM mahasiswa: ")
    nilai_mahasiswa = int(input("Nilai mahasiswa: "))

    data_student["nama"] = nama_mahasiswa
    data_student["nim"] = nim_mahasiswa
    data_student["nilai"] = nilai_mahasiswa

    list_students.append(data_student)

    del data_student

    stopper = input("Apakah ada data mahasiswa lain yang ingin diinputkan? (ya/tidak): ").strip().lower()

    if stopper not in ("ya", "tidak"):
        while True:
            print("Jawabannya hanya boleh ya dan tidak! Mohon input ulang")

            stopper = input("Apakah ada data mahasiswa lain yang ingin diinputkan? (ya/tidak): ").strip().lower()
            if stopper in ("ya", "tidak"):
                break

    if stopper == "tidak":
        break


#process and analysis
total_mahasiswa = len(list_students)
nilai_tertinggi = None
nilai_terendah = None
mahasiswa_nilai_tertinggi = set()
mahasiswa_nilai_terendah = set()
rata_rata = 0
jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0
jumlah_lulus = 0
jumlah_tidak_lulus = 0


for student in list_students:

    for key, value in student.items():
        if key == "nilai":
            rata_rata += value

            if 85 <= value:
                grade_mhs = "A"
                jumlah_a+=1
            elif 75 <= value < 85:
                grade_mhs = "B"
                jumlah_b+=1
            elif 55 <= value < 75:
                grade_mhs = "C"
                jumlah_c+=1
            elif 40 <= value < 55:
                grade_mhs = "D"
                jumlah_d+=1
            else:
                grade_mhs = "E"
                jumlah_e+=1

            if grade_mhs in ("A", "B", "C"):
                status_mhs = "Lulus"
                jumlah_lulus+=1
            else:
                status_mhs = "Tidak Lulus"
                jumlah_tidak_lulus+=1


            if nilai_tertinggi == None and nilai_terendah == None:
                nilai_tertinggi = value
                nilai_terendah = value

            if nilai_tertinggi < value:
                nilai_tertinggi = value

            if nilai_terendah > value:
                nilai_terendah = value

rata_rata /= total_mahasiswa

for student in list_students:

    if student["nilai"] == nilai_tertinggi:
        mahasiswa_nilai_tertinggi.add(student["nama"])

    if student["nilai"] == nilai_terendah:
        mahasiswa_nilai_terendah.add(student["nama"])
    

#Output
print("===== Data Mahasiswa =====")
for student in list_students :

    for key, value in student.items():
        print(f"{key:10}: {value}")

        if key == "nilai":

            if 85 <= value:
                print(f"{"Grade":10}: A")
            elif 75 <= value < 85:
                print(f"{"Grade":10}: B")
            elif 55 <= value < 75:
                print(f"{"Grade":10}: C")
            elif 40 <= value < 55:
                print(f"{"Grade":10}: D")
            else:
                print(f"{"Grade":10}: E")


            if grade_mhs in ("A", "B", "C"):
                print(f"{"Status":10}: Lulus")
            else:
                print(f"{"Status":10}: Tidak Lulus")

print("===== Summary =====")
print(f"{"Total Mahasiswa":10}: {total_mahasiswa}")
print(f"{"Nilai Tertinggi":10}: {nilai_tertinggi} ")
print(f"{"Mahasiswa dengan nilai tertinggi":10}:")
for x in mahasiswa_nilai_tertinggi:
    print(f"- {x}")
print(f"{"Nilai Terendah":10}: {nilai_terendah} ")
print(f"{"Mahasiswa dengan nilai terendah":10}:")
for x in mahasiswa_nilai_terendah:
    print(f"- {x}")
print(f"{"Rata-rata":10}: {rata_rata}")
print(f"{"Jumlah A":10}: {jumlah_a}")
print(f"{"Jumlah B":10}: {jumlah_b}")
print(f"{"Jumlah C":10}: {jumlah_c}")
print(f"{"Jumlah D":10}: {jumlah_d}")
print(f"{"Jumlah E":10}: {jumlah_e}")
print(f"{"Jumlah lulus":10}: {jumlah_lulus}")
print(f"{"Jumlah tidak lulus":10}: {jumlah_tidak_lulus}")