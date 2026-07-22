loop_status = True
data_penjualan = {}

jml_terlaris = None
jml_tdk_laris = None

barang_laris = None
barang_tdk_laris = None

total_terjual = 0

# Input
while loop_status:
    barang = input("Nama barang: ").strip().lower()
    if barang in data_penjualan:
        while True:
            print("Nama barang sudah ada dalam data mohon ganti nama lain!")
            barang = input("Nama barang: ").strip().lower()


            if barang not in data_penjualan:
                break
             

    terjual = int(input("Jumlah terjual: "))
    if terjual < 0:
        while True:
            print("Jumlah terjual tidak boleh kurang dari 0!")
            terjual = int(input("Jumlah terjual: "))
            
            if terjual >= 0:
                break


        

    data_penjualan[barang] = terjual

    stopper = input("Apakah ada barang lain yang akan diinputkan? (ya/tidak): ").lower()

    if stopper != "ya" and stopper != "tidak":
        while True:
            print("Jawaban hanya boleh ya atau tidak!")
            stopper = input("Apakah ada barang lain yang akan diinputkan? (ya/tidak): ").lower()

            if stopper in ("ya", "tidak"):
                break
    
    if stopper == "tidak":
        loop_status = False



# process
for nama, jml in data_penjualan.items():
    
    if jml_terlaris == None or jml > jml_terlaris:
        barang_laris = nama
        jml_terlaris = jml

    if jml_tdk_laris == None or jml < jml_tdk_laris:
        barang_tdk_laris = nama
        jml_tdk_laris = jml
    
    total_terjual += jml

print("===== Data Summary ======")
print(f"Barang terlaris\t\t\t: {barang_laris}")
print(f"Jumlah terjual\t\t\t: {jml_terlaris}")
print(f"Barang paling sedikit terjual\t: {barang_tdk_laris}")
print(f"Jumlah terjual\t\t\t: {jml_tdk_laris}")
print(f"Total penjualan\t\t\t: {total_terjual}")



        