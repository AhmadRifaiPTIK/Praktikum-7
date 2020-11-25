# Interface
print("~~~~")
print("PROGRAM HITUNG RATA-RATA")
print("~~~~")

#Input angka

inputawal = 0
jumlahinput = 0
ulangi=True
while (ulangi == True):
    try:
        inputangka = int(input("Masukan Bilangan Bulat : "))
        inputawal += inputangka
        jumlahinput += 1
        inputjawaban = input("lagi (y/n) :")
        if(inputjawaban == 'y'):
            ulangi=True
        elif (inputjawaban == 'n'):
            ulangi=False
    except FileNotFoundError:
        print("Angka Bukan Bilangan Bulat")
        continue

ratarata = inputawal/jumlahinput

print("Rata Rata Adalah : ", ratarata)