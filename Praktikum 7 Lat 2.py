# Interface
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Menambahkan data pada file")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

# input file
isifile = input("Masukan Nama file : ")
try:
    file = open(isifile, "a")

except FileNotFoundError:
    print("File Tidak Ditemukan")
# Masukan Data

ulangi = True
while (ulangi == True):
    inputdata = input("Data yang mau ditambakan : ")
    file.write(inputdata)
    inputjawaban = input("Mau lagi (y/n) :")
    if inputjawaban == 'y':
        ulangi = True
    elif inputjawaban == 'n':
        ulangi = False
        break
file.close()