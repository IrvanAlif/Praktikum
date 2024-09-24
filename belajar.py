print("nama gua irvan alif ganteng") # memunculkan kata
nama_saya = "irvan"
print ("nama_saya") # variabel
print("gunakan pagar untuk komen dan penggunaan pagar tidak akan di print" )

nama = "irvan alif" # string
usia = 19 # integer
tinggi_badan = 146.5 # penggunaan koma/desimal (float)
menyapa = "halo aku "
punya_pacar = False # penggunaan True & False untuk benar atau salah (huruf awal harus kapital)
punya_pacar = True # contoh ini kondisi 1 bulan kemudian dan yang di atas kondisi sebelumnya 

print(menyapa + nama) # gunakan tanda plus untuk menggabungkan varibel
print("halo aku " + nama) # bisa juga seperti ini
# tipe data yang berbeda tidak bisa langsung di gabung, jadi harus di konversi terlebih dahulu(samakan)
print(nama + str(usia))# penggunaan str,int,float untuk mengubah tipe datanya
print("tinggi saya " + str(tinggi_badan))
print(punya_pacar)

tanya_nama = input("siapa nama kamu?")#penggunaan input agar hasil codingan bisa di isi/ngetik
print(tanya_nama)

a = 50
b = 30
c = a + b # penggunaan + - * / sebagai tambah, kurang, kali, bagi
print(c)
#bisa juga dengan
A = input("masukkan angka pertama :")
B = input("masukkan angka kedua :")
c = int(A) // int(B) # ingat karena berbeda tipe data harus di samakan # tambahan garis miring agar hassil bagi di bulatkan 
print(c)
print("hasilnya adalah " + str(c))# bisa seperti ini

nama_kucingku = "bulldozer"
print( "bull" in nama_kucingku)#in untuk mengecek apakah ada kata di sana
print(nama_kucingku. count("bull"))# mengecek ada berapa kata 

# == sama dengan
# > lebih dari
# > kurang dari
# ! tidak sama dengan
# >= lebih dari sama dengan
# <= kurang dari sama dengan 
# : maka

usia_gua = 19
if usia_gua > 15:#penggunaan jika 
    print("aku dewasa")
    print("masih smk")
elif usia_gua > 15 and usia_gua < 19:#mengecek kondisi
    print("masih smk")
else:
    print("gak masuk")#jika tidak ada dalam pilihan dan kondisi di atas
    
pacar_gua = ["cewek", "perempuan", "wanita"] #gunakan kurung kotak

print(pacar_gua)
print(len(pacar_gua))#untuk menghitung jumlah nya
for pacar in pacar_gua :#menggunakan for & in untuk memecah jadi 1 per 1
    print(pacar)
    
awal = 2
while awal <= 10 : #penggunaan while untuk pengonddisian sementara itu
    print(awal)
    awal = awal + 1
    
saldo_awal = 5000
deposit = input("masukkan jumlah deposit mu :" )
banyak_uang = saldo_awal + int(deposit) 
hutang = 50000
bayar_utang = banyak_uang - hutang
if bayar_utang >= 50000 :
    print("utang lunas")
else :
    print("masih berutang sebanyak" + str(bayar_utang))