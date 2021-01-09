from datetime import * #impoer modul datetime untuk operasi / tampilan yang membutuhkan tanggal bulan tahun dan waktu
myfile = open("dataKaryawan.dat", "a") #buka file data karyawab dengan mode sesuai kondisi

def addKaryawan(nip, nama, alamat, gol, tgllahir, umur) : #deklarasikan nama function beserta parameternya (void)
    listData = [nip, nama, alamat, gol.upper(), tgllahir, str(umur) + "\n"] #isi dari listdata (uban paramater ker data list)
    myfile.write("|".join(listData)) #tuliskan data diatas ke dalam file dan beri pembatas "|"

def getUsia(tgl) :    #deklarasikan nama function beserta parameternya (non void)
    listTgl = tgllahir.split("-") #isi dari listTanggal adalah parameter tanggal lahir yang datanya sudah dipisah dengan split oleh karakter "-"
    thnlahir = int(listTgl[0]) #inputan tanggal lahir diambil dari listTgl data pertama
    thnskrg = datetime.now() #thnskrg diambil dwaktu saat ini dengan datetime.now
    umur = thnskrg.year - thnlahir #dapatkan umur dengan pengurangan thnskrg dengan thllahir
    return umur #mengembalikan nilai untuk menyimpannya

while True :   #perulangan inputan data sesuai keinginan user dengan while (karna jumlah belum diketahui)
    nip = input("\nMasukkan NIP : ") #input nip
    nama = input("Masukkan Nama : ") #ini untuk inputan nama
    alamat = input("Masukkan Alamat : ") #ini untuk inputan alamat
    gol = input("Masukkan Golongan (A / B / C) : ")  #ini untuk input golongan

    if(gol.lower() == "a" or gol.lower() == "b" or gol.lower() == "c") : #jika inputan golongan diisi dengan A/B/C/a/b/c maka
        tgllahir = input("Masukkan Tgl Lahir (Format yyyy-mm-dd) : ") #inputan untuk variabel tgllahir
        umur = getUsia(tgllahir) #isi nilai variabel umur dengan panggil function getUsia dan isi parameternya dengan inputan tgl lahir
        try : #tandai blok yang akan dicek exception
            if(datetime.strptime(tgllahir, "%Y-%m-%d")) :
                tambah = input("\nTambah data (y / n) : ") #konfirmasikan apakah user mau mengulang inputan
                if(tambah.lower() == "y") : #jika inputannya "y" maka
                    addKaryawan(nip,nama,alamat,gol,tgllahir,umur) #tambahkan data yang sudah diisikan sebelumnya
                    continue #lalu lanjutkan inputan NIP, Nama, Alamat, Gol
                elif(tambah.lower() == "n") : #jika inputannya "n" maka
                    addKaryawan(nip,nama,alamat,gol,tgllahir,umur) #tambahkan data yang sudah diisikan sebelumnya
                    break  #lalu hentikan perulangan            
                else : #jika inputnya bukan "y"/"n" maka
                    print("Maaf ! Inputan yang anda masukkan Tidak Valid") #tampilan pesan dalam kurung print
                    addKaryawan(nip,nama,alamat,gol,tgllahir,umur) #tambahkan data yang sudah diisikan sebelumnya
                    break   #lalu hentikan perulangan    

        except ValueError : #jika muncul exception ValueError maka 
            print("Maaf ! Inputan yang anda masukkan tidak Valid") #akan ditampilkan pesan dalam kurung print
            continue  #lalu lanjutkan inputan ke konfirmasi tambah data lagi
    else : #jika inputan golongan yang dimasukkan salah maka
        print("Maaf ! Inputan yang anda masukkan tidak Valid") #akan ditampilkan pesan dalam kurung print
        continue #lalu lanjutkan inputan ke tambah tgllahir

myfile.close() #tutup file untuk mencegah file corrupted atau strukturnya rusak      