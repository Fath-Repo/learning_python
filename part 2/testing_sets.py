set_bahasa = set()

while True:
    bahasa = input("Bahasa pemrograman favorit mahasiswa: ")

    set_bahasa.add(bahasa)

    stopper = input("Apakah masih ada bahasa lain? (ya/tidak): ").strip().lower()
    if stopper not in ("ya", "tidak"):
        while True:
            print("Jawaban hanya boleh ya dan tidak")

            stopper = input("Apakah masih ada bahasa lain? (ya/tidak): ").strip().lower()
            if stopper in ("ya","tidak"):
                break

    if stopper == "tidak":
        break

print("===== Summary =====")
print("Bahasa unik pilihan mahasiswa: ")
for x in set_bahasa:
    print(x)

print(f"Jumlah bahasa unik yang di pilih mahasiswa: {len(set_bahasa)}")


            