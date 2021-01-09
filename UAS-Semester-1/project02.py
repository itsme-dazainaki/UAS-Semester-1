file = open("dataKaryawan.dat", "r")  #buka file data karyawan dengan mode read, untuk membaca isi file
isi = file.readlines() #ini syntax untuk membaca file text yang ada di atas
kode = input("Masukkan Kode Karyawan : ") #ini untuk inputan kode karyawan

def getGapok(gol) :  #deklarasikan nama function beserta parameternya (non void)
    if(gol == "A") : #jika nilai parameternya "A" maka
        gapok = 4000000
    elif(gol == "B") :  #jika nilai parameternya "B" maka
        gapok = 4500000
    elif(gol == "C") :  #jika nilai parameternya "C" maka
        gapok = 5000000
    return gapok #mengembalikan nilai untuk menyimpannya

data = {} #deklarasikan sebuah dictionary kosong
try : #tandai blok yang akan dicek exception
    for i in range(len(isi)) : #perulangan untuk variabel in dalam range dari isi 
            a = isi[i].replace("\n", "") #
            b = a.split("|")        
            data[kode] = [b[1], b[2], b[3], b[4], b[5]]
    gaji = getGapok(data[kode][2])
        
    print("\nKode Karyawan   : ", kode) #tampilkan kode karyawan isinya variabel kode
    print("Nama Karyawan   : ", data[kode][0]) #tampilkan nama karyawan, isinya data yang ada didictionary (data) dengan key (kode) nomor indeksnya 0/data pertama
    print("Alamat          : ", data[kode][1]) #tampilkan alamat, isinya data yang ada didictionary (data) dengan key (kode) nomor indeksnya 1/data kedua
    print("Golongan        : ", data[kode][2]) #tampilkan golongan, isinya data yang ada didictionary (data) dengan key (kode) nomor indeksnya 2/data ketiga
    print("Gaji Pokok      : Rp ", gaji) #tampilkan gaji pokok, dengan isi variabel "gaji"
    print("Tanggal Lahir   : {0} (Usia : {1})".format(data[kode][3], data[kode][4])) #tampilkan tgl lahir dan usia dari data yang ada didictionary (data) dengan key (kode) nomor indeks 3 & 4 data ke 4 dan 5

except NameError : #jika muncul exception ValueError maka 
    print("Maaf ! Data tidak Ditemukan") #akan ditampilkan pesan dalam kurung print