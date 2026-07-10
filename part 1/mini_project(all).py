jmlMhs = int(input("Berapa jumlah mahasiswa: "))
passedCount = 0
failedCount = 0
bobotTgs = 0.2
bobotKuis = 0.2
bobotUts = 0.25
bobotUas = 0.35

for i in range(jmlMhs):
    nama = input("Nama: ")

    nilaiTgs = float(input("Nilai tugas: "))
    if nilaiTgs < 0 or nilaiTgs > 100:
        print("Nilai tugas tidak boleh kurang dari 0 atau lebih dari 100")
        print("Akan melanjutkan ke mahasiswa selanjutnya")
        continue   
    nilaiKuis = float(input("Nilai kuis: "))
    if nilaiKuis < 0 or nilaiKuis > 100:
        print("Nilai kuis tidak boleh kurang dari 0 atau lebih dari 100")
        print("Akan melanjutkan ke mahasiswa selanjutnya")
        continue   
    nilaiUts = float(input("Nilai UTS: "))
    if nilaiUts < 0 or nilaiUts > 100:
        print("Nilai UTS tidak boleh kurang dari 0 atau lebih dari 100")
        print("Akan melanjutkan ke mahasiswa selanjutnya")
        continue   
    nilaiUas = float(input("Nilai UAS: "))
    if nilaiUas < 0 or nilaiUas > 100:
        print("Nilai UAS tidak boleh kurang dari 0 atau lebih dari 100")
        print("Akan melanjutkan ke mahasiswa selanjutnya")
        continue   

    nilaiTgs *= bobotTgs
    nilaiKuis *= bobotKuis
    nilaiUts *= bobotUts
    nilaiUas *= bobotUas
    nilaiAkhir = nilaiTgs + nilaiKuis + nilaiUts + nilaiUas

    if 85 <= nilaiAkhir:
        grade = "A"
        predikat = "Sangat memuaskan"
    elif 75 <= nilaiAkhir < 85:
        grade = "B"
        predikat = "Memuaskan"
    elif 55 <= nilaiAkhir < 75:
        grade = "C"
        predikat = "Cukup"
    elif 40 <= nilaiAkhir < 55:
        grade = "D"
        predikat = "Kurang"
    else:
        grade = "E"
        predikat = "Sangat kurang"


    if grade in ("A", "B", "C"):
        status = "Lulus"
        passedCount+=1
    else:
        status = "Tidak Lulus"
        failedCount+=1

    print("===== Hasil Penilaian =====")

    print(f"Nama: {nama}")
    print(f"Nilai akhir: {nilaiAkhir}")
    print(f"Grade: {grade} -> {predikat}")
    print(f"Status: {status}")

    if nilaiAkhir < 55:
        print("Mahasiswa disarankan mengikuti program remedial.")
    
    print("==========================")
    print()

print(f"Jumlah mahasiswa lulus: {passedCount}")
print(f"Jumlah mahasiswa tidak lulus: {failedCount}")