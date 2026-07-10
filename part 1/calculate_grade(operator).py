#Input
tugas = int(input("Tugas: "))
kuis = int(input("Kuis: "))
uts = int(input("UTS: "))
uas = int(input("UAS: "))

#Validation and Process
if (0 <= tugas <= 100 and 0 <= kuis <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
    nilaiAkhir = (tugas * 0.2) + (kuis * 0.2) + (uts * 0.25) + (uas * 0.35)
else:
    print("Nilai harus berada pada rentang 0 sampai 100")

#Output
print(f"Nilai Akhir: {nilaiAkhir}")

