#Masukan File
isifile = input("Masukan Nama File:")

#Rumus Output file

try:
    file = open(isifile , "r")
    print("Isi File", isifile, "adalah")
    print(file.read())

except FileNotFoundError:
    print("File Tidak Ditemukan")


