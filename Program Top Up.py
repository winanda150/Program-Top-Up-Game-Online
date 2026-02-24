# Program Top Up Winanda Store
# Program ini adalah aplikasi untuk melakukan top up game online

# library atau module yang digunakan
import getpass, time, os

# banner program
banner = (
    "===== Selamat Datang di Winanda Store =====\n"
    "Pilih Opsi Berikut :\n"
    "1. Login\n"
    "2. Register"
)

# list jenis top up
listproduk = [
    "Top Up Mobile Legends",
    "Top Up Free Fire Max",
    "Top Up Super Sus",
    "Top Up Call Of Duty Mobile"
]

# Menyimpan data transaksi
dict_trx = {}

# metode pembayaran
metode_pembayaran = {
    1:"Qris",
    2:"Kartu Kredit",
    3:"Virtual Account",
    4:"Bank Transfer",
}

# list admin
list_admin = {
    1:"Winanda",
    2:"Reva",
    3:"Gustadi",
}
# harga top up game mlbb
hargatopupmlbb = {
    1: 26000,
    2: 78000,
    3: 130000,
    4: 150000,
    5: 1500,
    6: 12000,
    7: 22000,
    8: 44000,
    9: 76000,
    10: 105000,
    11: 143000,
    12: 219000,
    13: 475000
}

# harga top up game ffmax
hargatopupff = {
    1: 1500,
    2: 10000,
    3: 20000,
    4: 45000,
    5: 90000,
    6: 180000,
    7: 270000,
    8: 450000
}

# harga top up game sus
hargatopupsus = {
    1: 10000,
    2: 35000,
    3: 57000,
    4: 117000,
    5: 240000,
    6: 613000,
    7: 73000,
    8: 128000,
    9: 13000,
    10: 134000,
    11: 157000
}

# harga top up game codm
hargatopupcodm = {
    1: 10000,
    2: 18000,
    3: 45000,
    4: 90000,
    5: 180000,
    6: 270000,
    7: 450000,
    8: 900000
}

# fungsi utama program
def main():
    print(banner) # menampilkan banner
    while True: # loop untuk mengulangi terus menerus
        try: # menangani error input
            opsi = int(input("Opsi : ")) # input opsi
        except ValueError: # jika input bukan angka
            print("Masukkan angka 1 atau 2!") # menampilkan pesan error
            continue # lanjut ke loop berikutnya ke input ulang
        # cek opsi
        if opsi == 1: # jika opsi 1
            time.sleep(1) # jeda 1 detik
            login() # panggil fungsi login
            break # keluar dari loop
        elif opsi == 2: # jika opsi 2
            time.sleep(1) # jeda 1 detik
            register() # panggil fungsi register
            break # keluar dari loop
        else: # jika opsi bukan 1 atau 2
            print("Pilihan tidak tersedia, coba lagi!") # menampilkan pesan error

# fungsi login
def login():
    print("========= Login di Winanda Store ==========") # menampilkan banner login
    username = input("Masukkan username : ") # input username
    cekuser = False
    try:
        with open("Akun.txt", "r") as file:
            for cek in file:
                user, _ = cek.strip().split(",")
                if user == username:
                    cekuser = True
                    file.close()
                    break
    except FileNotFoundError:
        pass
    if not cekuser:
        print(f"Username {username} belum terdaftar")
        main()
        return
    password = getpass.getpass("Masukkan Kata Sandi : ") # input password
    print("Loading...") # menampilkan pesan loading
    time.sleep(4) # jeda 4 detik
    verifikasi = False # set verifikasi ke False
    # cek username dan password di file HTML
    try: # menangani error file tidak ditemukan
        with open("Akun.txt", "r") as file: # buka file HTML
            for line in file: # loop untuk setiap baris di file
                user, pwd = line.strip().split(",") # pisahkan username dan password
                if user == username and pwd == password: # cek username dan password
                    verifikasi = True # set verifikasi ke True
                    file.close() # tutup file
                    break # keluar dari loop
    except FileNotFoundError: # jika file tidak ditemukan
        pass # lewati
    # cek verifikasi
    if verifikasi: # jika verifikasi True
        print("Login berhasil...") # menampilkan pesan login berhasil
        time.sleep(2) # jeda 2 detik
        print(f"Selamat datang di Winanda Store!") # menampilkan pesan selamat datang
        print(f"Username : {username}") # menampilkan username
        menu(username) # panggil fungsi menu
    else: # jika verifikasi False
        print("Password yang anda masukkan salah. Silahkan coba lagi!") # menampilkan pesan error
        main() # panggil fungsi utama
        return # keluar dari fungsi

# fungsi register
def register():
    print("========= Register di Winanda Store ==========") # menampilkan banner register
    username = input("Masukkan username : ") # input username
    # cek apakah username sudah digunakan
    cekuser = False # set Used ke False
    try: # menangani error file tidak ditemukan
        with open("Akun.txt", "r") as file: # buka file TXT
            for cek in file: # loop untuk setiap baris di file
                user, _ = cek.strip().split(",") # pisahkan username dan password
                if user == username: # cek username
                    cekuser = True # set Used ke True
                    file.close() # tutup file
                    break # keluar dari loop
    except FileNotFoundError: # jika file tidak ditemukan
        pass # lewati
    # cek apakah username sudah digunakan
    if cekuser: # jika Used True
        print("Username sudah digunakan, silahkan pilih yang lain.") # menampilkan pesan error
        main() # panggil fungsi utama
        return # keluar dari fungsi

    password = getpass.getpass("Masukkan Kata Sandi : ") # input password
    confirm = getpass.getpass("Konfirmasi Kata Sandi : ") # input konfirmasi password
    print("Loading...") # menampilkan pesan loading
    time.sleep(5) # jeda 5 detik
    # cek apakah password dan konfirmasi password sama
    if password != confirm: # jika tidak sama
        print("Password tidak sama, registrasi dibatalkan.") # menampilkan pesan error
        main() # panggil fungsi utama
        return # keluar dari fungsi
    # simpan username dan password ke file TXT
    with open("Akun.txt", "a") as file: # buka file TXT
        file.write(f"{username},{password}\n") # tulis username dan password ke file
        file.close() # tutup file
    print("Register Telah Berhasil! Silahkan Login.") # menampilkan pesan register berhasil
    time.sleep(2) # jeda 2 detik
    main() # panggil fungsi utama
    return # keluar dari fungsi

# fungsi menu
def menu(username): # menerima parameter username
    print("===== Top Up Winanda Store =====") # menampilkan banner menu
    print("Silahkan pilih jenis top up berikut :") # menampilkan pesan pilih jenis top up
    print("1. Top Up Game") # menampilkan opsi top up game
    print("2. Logout") # menampilkan opsi logout
    print("3. Hapus Akun") # menampilkan opsi hapus akun
    if username in list_admin.values():
        print("4. Menu Admin") # menampilkan opsi menu admin
    while True: # loop untuk mengulangi terus menerus
        try: # menangani error input
            if username in list_admin.values():
                idproduk = int(input("Pilih produk (1-4): "))
            else:
                idproduk = int(input("Pilih produk (1-3): ")) # input opsi
        except ValueError: # jika input bukan angka
            if username in list_admin.values():
                print("Masukkan angka 1 - 4!")
            else:
                print("Masukkan angka 1 - 3!") # menampilkan pesan error
            continue # lanjut ke loop berikutnya ke input ulang
        # cek opsi
        if idproduk == 1: # jika opsi 1
            time.sleep(2) # jeda 2 detik
            topupgame(username) # panggil fungsi topupgame
            break # keluar dari loop
        elif idproduk == 2: # jika opsi 2
            time.sleep(2) # jeda 2 detik
            print(f"Anda telah logout dari Akun username {username}") # menampilkan pesan logout
            time.sleep(2) # jeda 2 detik
            main() # panggil fungsi utama
            break # keluar dari loop
        elif idproduk == 3: # jika opsi 3
            time.sleep(2) # jeda 2 detik
            hapus_akun(username) # panggil fungsi hapus_akun
            break # keluar dari loop
        elif idproduk == 4 and username in list_admin.values():
            time.sleep(2) # jeda 2 detik
            admin_menu(username) # panggil fungsi admin_menu
            break # keluar dari loop
        else: # jika opsi bukan 1, 2, atau 3
            print("Pilihan tidak tersedia, coba lagi!") # menampilkan pesan error

def admin_menu(username):
    print("===== Menu Admin Winanda Store =====")
    print("1. Lihat Semua Akun")
    print("2. Kembali ke Menu Utama")
    print("3. Lihat Akun Admin")
    while True:
        try:
            pilih = int(input("Masukkan pilihan anda : "))
        except ValueError:
            print("Masukkan angka 1 - 2!")
            continue
        if pilih == 1:
            time.sleep(1)
            lihatakun(username)
            break
        elif pilih == 2:
            time.sleep(1)
            menu(username)
            break
        elif pilih == 3:
            time.sleep(1)
            lihatadmin(username)
        else:
            print("Opsi tidak tersedia, coba lagi!")

def lihatakun(username):
    try:
        with open("Akun.txt", "r") as file:
            print("Akun Terdaftar :")
            for i in file:
                user = i.strip().split(",")[0]
                print(f"Username : {user}")
        opsi = input("Apakah anda ingin kembali ke menu admin? (Y) : ")
        if opsi == "y" or opsi == "Y":
            admin_menu(username)
            return
        else:
            print("Opsi tidak tersedia, coba lagi!")
    except FileNotFoundError:
        print("Akun tidak ditemukan")
        pass

def lihatadmin(username):
    try:
        with open("Akun.txt", "r") as file:
            print("Akun Terdaftar :")
            for i in file:
                user = i.strip().split(",")[0]
                if user in list_admin.values():
                    print(f"Username : {user}")
                else:
                    pass
        opsi = input("Apakah anda ingin kembali ke menu admin? (Y) : ")
        if opsi == "y" or opsi == "Y":
            admin_menu(username)
            return
        else:
            print("Opsi tidak tersedia, coba lagi!")
    except FileNotFoundError:
        print("Akun tidak ditemukan")
        pass

# fungsi topupgame
def topupgame(username): # menerima parameter username
    print("===== Winanda Store =====") # menampilkan banner topupgame
    print("Silahkan pilih jenis top up game berikut :") # menampilkan pesan pilih jenis top up game
    for id, produk in enumerate(listproduk, 1): # loop untuk setiap produk di listproduk
        print(f"{id}. {produk}") # menampilkan opsi produk
    while True: # loop untuk mengulangi terus menerus
        try: # menangani error input
            produkid = int(input("Masukkan jenis top up (1-4) : ")) # input opsi
        except ValueError: # jika input bukan angka
            print("Masukkan angka 1 - 4!") # menampilkan pesan error
            continue # lanjut ke loop berikutnya ke input ulang
        # cek opsi
        dict_trx["produkid"] = produkid # simpan produkid ke dict_trx
        if produkid == 1: # jika opsi 1
            time.sleep(2) # jeda 2 detik
            mlbb(username) # panggil fungsi mlbb dengan parameter username
            break # keluar dari loop
        elif produkid == 2: # jika opsi 2
            time.sleep(2) # jeda 2 detik
            ffmax(username) # panggil fungsi ffmax dengan parameter username
            break # keluar dari loop
        elif produkid == 3: # jika opsi 3
            time.sleep(2) # jeda 2 detik
            sus(username) # panggil fungsi sus dengan parameter username
            break # keluar dari loop
        elif produkid == 4: # jika opsi 4
            time.sleep(2) # jeda 2 detik
            codm(username) # panggil fungsi codm dengan parameter username
            break # keluar dari loop
        else: # jika opsi bukan 1, 2, 3, atau 4
            print("Pilihan tidak tersedia, coba lagi!") # menampilkan pesan error

# fungsi mlbb
def mlbb(username): # menerima parameter username
    print("===== Selamat Datang di Top Up Mobile Legends =====") # menampilkan banner mlbb
    print("1. Masukkan User ID") # menampilkan pesan masukkan user id
    while True: # loop untuk mengulangi terus menerus
        try: # menangani error input
            idmlbb = int(input("Masukkan Id ML : ")) # input user id
            zonemlbb = int(input("Masukkan Id Zone : ")) # input zone id
        except ValueError: # jika input bukan angka
            print("Masukkan angka!") # menampilkan pesan error
            continue # lanjut ke loop berikutnya ke input ulang
        dict_trx["idmlbb"] = idmlbb # simpan idmlbb ke dict_trx
        dict_trx["zonemlbb"] = zonemlbb # simpan zonemlbb ke dict_trx
        break # keluar dari loop
    time.sleep(1) # jeda 1 detik
    print("2. Pilih Nominal Top Up") # menampilkan pesan pilih nominal top up
    print("===== Weekly Diamond Pass =====") # menampilkan banner weekly
    wdp = [ # untuk menampilkan list data wdp
        "1. 1x Weekly Diamond Pass",
        "2. 3x Weekly Diamond Pass",
        "3. 5x Weekly Diamond Pass",
        "4. Twilight Pass",
    ]
    for item in wdp: # loop untuk item di dalam data wdp
        print(item) # menampilkan di dalam item
    time.sleep(1) # jeda 1 detik
    print("=========== Diamond ===========") # menampilkan banner diamond
    dm = [ # untuk menampilkan list data dm
        "5. 5 Diamond",
        "6. 44 Diamond",
        "7. 85 Diamond",
        "8. 170 Diamond",
        "9. 296 Diamond",
        "10. 408 Diamond",
        "11. 568 Diamond",
        "12. 875 Diamond",
        "13. 2010 Diamond",
    ]
    for item in dm: # loop untuk item di dalam data dm
        print(item) # menampilkan di dalam item
    all_produkmlbb = wdp + dm # menyimpan data wdp dan dm ke variabel all_produkmlbb
    while True: # loop untuk mengulangi terus menerus
        try: # menangani error input
            opsi1 = int(input("Masukkan id produk : ")) # input opsi
        except ValueError: # jika input bukan angka
            print("Masukkan angka, bukan teks!") # menampilkan pesan error
            continue # lanjut ke loop berikutnya ke input ulang
        # cek opsi
        if 1 <= opsi1 <= len(all_produkmlbb): # jika opsi 1 sampai 13
            dict_trx["opsi1"] = opsi1 # simpan produkid ke dict_trx
            break # keluar dari loop
        else: # jika opsi bukan 1 sampai 13
            print("id produk tidak tersedia, silahkan coba lagi!") # menampilkan pesan error
    
    print("===========================") # menampilkan pesan semacam pembatas
    time.sleep(1) # jeda 1 detik
    print("3. Pilih Jumlah Pembelian") # menampilkan pesan pilih jumlah pembelian
    while True: # loop untuk mengulangi terus menerus
        try: # menangani error input
            jumlah = int(input("Masukkan jumlah pembelian (1-10): ")) # input opsi
        except ValueError: # jika input bukan angka
            print("Masukkan angka, bukan teks!") # menampilkan pesan error
            continue # lanjut ke loop berikutnya ke input ulang
        if 1 <= jumlah <= 10: # jika opsi 1 sampai 10
            dict_trx["jumlah"] = jumlah # simpan jumlah ke dict_trx
            break # keluar dari loop
        else: # jika opsi bukan 1 sampai 10
            print("Jumlah produk telah maksimum, silahkan coba lagi!") # menampilkan pesan error
    metodepembayaran(hargatopupmlbb, all_produkmlbb, username) # jika input benar panggil fungsi metodepembayaran dengan parameter

# fungsi ffmax
def ffmax(username): # menerima parameter username
    print("===== Selamat Datang di Top Up Free Fire Max =====") # menampilkan banner ff max
    print("1. Masukkan Player ID") # menampilkan pesan masukkan player id
    while True: # loop untuk mengulangi terus menerus
        try: # menangani error input
            idff = int(input("Masukkan Id FF : ")) # input user id
        except ValueError: # jika input bukan angka
            print("Masukkan angka, bukan teks") # menampilkan pesan error
            continue # lanjut ke loop berikutnya ke input ulang
        dict_trx["idff"] = idff # simpan idff ke dict_trx
        break # keluar dari loop
    time.sleep(1) # jeda 1 detik
    print("2. Pilih Nominal Top Up") # menampilkan pesan nominal top up
    print("======= Diamond =======") # menampilkan banner diamond
    dmff = [ # untuk menampilkan list data dmff
        "1. 5 Diamond",
        "2. 50 Diamond",
        "3. 140 Diamond",
        "4. 355 Diamond",
        "5. 720 Diamond",
        "6. 1450 Diamond",
        "7. 2180 Diamond",
        "8. 3640 Diamond",
    ]
    for item in dmff:
        print(item)
    all_produkff = dmff
    while True:
        try:
            opsi1 = int(input("Masukkan id produk : "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        if 1 <= opsi1 <= len(all_produkff):
            dict_trx["opsi1"] = opsi1
            break
        else:
            print("id produk tidak tersedia, silahkan coba lagi!")
    
    print("===========================")
    time.sleep(1)
    print("3. Pilih Jumlah Pembelian")
    while True:
        try:
            jumlah = int(input("Masukkan jumlah pembelian (1-10): "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        if 1 <= jumlah <= 10:
            dict_trx["jumlah"] = jumlah
            break
        else:
            print("Jumlah produk telah maksimum, silahkan coba lagi!")
    metodepembayaran(hargatopupff, all_produkff, username)

def sus(username):
    print("===== Selamat Datang di Top Up Super Sus =====")
    print("1. Masukkan ID Space")
    while True:
        try:
            idsus = int(input("Masukkan Id Space : "))
        except ValueError:
            print("Masukkan angka, bukan teks")
            continue
        dict_trx["idsus"] = idsus
        break
    time.sleep(1)
    print("2. Pilih Nominal Top Up")
    print("======= Diamond =======")
    dmsus = [
        "1. 100 Goldstar",
        "2. 310 Goldstar",
        "3. 520 Goldstar",
        "4. 1060 Goldstar",
        "5. 2180 Goldstar",
        "6. 5600 Goldstar",
        "7. Super Pass",
        "8. Super Pass Bundle",
        "9. Weekly Card",
        "10. Monthly Card",
        "11. Super VIP Card",
    ]
    for Goldstart in dmsus:
        print(Goldstart)
    all_produksus = dmsus
    while True:
        try:
            opsi1 = int(input("Masukkan id produk : "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        if 1 <= opsi1 <= len(all_produksus):
            dict_trx["opsi1"] = opsi1
            break
        else:
            print("id produk tidak tersedia, silahkan coba lagi!")
    
    print("===========================")
    time.sleep(1)
    print("3. Pilih Jumlah Pembelian")
    while True:
        try:
            jumlah = int(input("Masukkan jumlah pembelian (1-10): "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        if 1 <= jumlah <= 10:
            dict_trx["jumlah"] = jumlah
            break
        else:
            print("Jumlah produk telah maksimum, silahkan coba lagi!")
    metodepembayaran(hargatopupsus, all_produksus, username)

def codm(username):
    print("===== Selamat datang di Top Up Call Of Duty Mobile =====")
    print("1. Masukkan PlayerID")
    while True:
        try:
            idcodm = int(input("Masukkan PlayerID : "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        dict_trx["idcodm"] = idcodm
        break
    time.sleep(1)
    print("2. Pilih Nominal Top Up")
    print("======= CP =======")
    cpcodm = [
        "1. 63 CP",
        "2. 128 CP",
        "3. 321 CP",
        "4. 645 CP",
        "5. 1373 CP",
        "6. 2060 CP",
        "7. 3564 CP",
        "8. 7656 CP",
    ]
    for CP in cpcodm:
        print(CP)
    allprodukcodm = cpcodm
    while True:
        try:
            opsi1 = int(input("Masukkan id produk : "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        if 1 <= opsi1 <= len(allprodukcodm):
            dict_trx["opsi1"] = opsi1
            break
        else:
            print("id produk tidak tersedia, silahkan coba lagi")
    
    print("===========================")
    time.sleep(1)
    print("3. Pilih Jumlah Pembelian")
    while True:
        try:
            jumlah = int(input("Masukkan jumlah pembelian (1-10): "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        if 1 <= jumlah <= 10:
            dict_trx["jumlah"] = jumlah
            break
        else:
            print("Jumlah produk telah maksimum, silahkan coba lagi!")
    metodepembayaran(hargatopupcodm, allprodukcodm, username)

def hapus_akun(username):
    print("===== Hapus Akun Winanda Store =====")
    while True:
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus akun {username}? (Y/N): ")
        if konfirmasi == "y" or konfirmasi == "Y":
            try:
                with open("Akun.txt", "r") as f:
                    lines = f.readlines()
                with open("Akun.txt", "w") as f:
                    for line in lines:
                        if not line.startswith(username + ","):
                            f.write(line)
                print("Akun berhasil dihapus.")
            except FileNotFoundError:
                print("Data akun tidak ditemukan.")
            main()
            break
        elif konfirmasi == "n" or konfirmasi == "N":
            print("Anda membatalkan penghapusan akun")
            time.sleep(2)
            menu(username)
            break
        else:
            print("Input tidak valid. Silakan masukkan Y atau N.")

def metodepembayaran(harga_dict, produk_list, username):
    print("===========================")
    time.sleep(1)
    print("4. Pilih Metode Pembayaran")
    for id, name in metode_pembayaran.items():
        print(f"{id}. {name}")
    while True:
        try:
            pembayaran = int(input("Masukkan metode pembayaran (1-4): "))
        except ValueError:
            print("Masukkan angka, bukan teks!")
            continue
        if 1 <= pembayaran <= len(metode_pembayaran):
            dict_trx["pembayaran"] = pembayaran
            break
        else:
            print("Metode Pembayaran tidak tersedia, silahkan coba lagi!")

    print("Loading...")
    time.sleep(3)
    produk_nama = produk_list[dict_trx['opsi1'] - 1].split('. ', 1)[-1]
    jumlah = dict_trx.get("jumlah", 1)
    harga_satuan = harga_dict[dict_trx["opsi1"]]
    total = harga_satuan * jumlah
    # Pajak sesuai metode pembayaran
    pajak_persen = {
        1: 850,   # Qris pajak tetap
        2: 2050,   # Kartu Kredit
        3: 2550,   # Virtual Account
        4: 1500    # Bank Transfer
    }
    pajak = pajak_persen.get(pembayaran, 0)
    nama_produk = listproduk[dict_trx["produkid"] - 1]

    # Tampilkan detail transaksi
    print("======= Detail Pesanan =======")
    print(f"Top Up : {nama_produk.replace('Top Up ', '')}")
    print(f"Username : {username}")

    # Tampilkan ID Sesuai Game
    if "idmlbb" in dict_trx:
        print(f"User Id : {dict_trx['idmlbb']}")
    if "zonemlbb" in dict_trx:
        print(f"ID Zone : {dict_trx['zonemlbb']}")
    if "idff" in dict_trx:
        print(f"User Id : {dict_trx['idff']}")
    if "idsus" in dict_trx:
        print(f"User Id : {dict_trx['idsus']}")
    if "idcodm" in dict_trx:
        print(f"User Id : {dict_trx['idcodm']}")

    print(f"Produk : {produk_nama}")
    print(f"Jumlah Pembelian : {jumlah} Produk")
    print(f"Metode Pembayaran : {metode_pembayaran[pembayaran]}")
    print(f"Harga Satuan : Rp {harga_satuan:,}")
    print(f"Subtotal : Rp {total:,}")
    print(f"Pajak : Rp {pajak:,}")
    print(f"Total Pembayaran : Rp {total + pajak:,}")
    print(f"=================================")

    time.sleep(1)
    while True:
        konfirmasi = input("Apakah anda yakin dengan data tersebut? (Y/N): ")
        if konfirmasi == "y" or konfirmasi == "Y":
            print("Memproses transaksi...")
            time.sleep(6)
            print("Transaksi berhasil!")
            print("Silahkan cek akun anda untuk melihat top up yang sudah masuk")
            print("Terima kasih telah bertransaksi di Winanda Store!")
            dict_trx.clear()
            break
        elif konfirmasi == "n" or konfirmasi == "N":
            time.sleep(3)
            print("Anda membatalkan transaksi")
            dict_trx.clear()
            menu(username)
            return
        else:
            print("Input tidak valid. Silakan masukkan Y atau N.")

if __name__ == "__main__":
    os.system("cls")
    main()