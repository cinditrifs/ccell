# Candy Cell 
Aplikasi dekstop yang digunakan oleh admin dan juga agen. 

### Pengguna
Admin:
- Dapat melihat, , mengedit, menghapus dan juga menambah daftar daftar agen (on proses)
- Dapat melihat, mengedit, menghapus dan juga menambah daftar harga/paket (on process)
- Melihat riwayat transfer (on process)
- Transfer saldo

Agen:
- Dapat melihat daftar harga/paket
- Dapat melakukan transaksi pulsa
- Dapat melihat history transaksi (on process)

### Yang harus dipersiapkan 
- Python 3.5+
- Redis
- Redis dekstop manager (conditional, untuk dapat melihat data yang kita simpan)
- Library Python : redis, tkinter

### Cara menjalankan 
1. Unduh/clone repository ini.
2. Pastikan python, redis, redis desktop manager dan library yang diperlukan sudah terinstall. Untuk library dapat diinstall melalui cmd: ```pip install <nama library>``` 
3. Sebelum menjalankan program ini, pastikan anda sudah terhubung dengan server redis. 
4. Jalankan script ```main.py``` pada folder CandyCell. Script ini juga langsung menjalankan file ```database.py```
5. Login menggunakan akun yang tersedia pada ```daftarakun.txt``` 
6. Aplikasi dapat digunakan

### note :
###### Redis dapat di download di > https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100
###### Redis dekstop manager di download di > https://github.com/uglide/RedisDesktopManager
###### Cara menghubungkan dengan server redis > buka file redis lalu ```redis server``` . Namun, jika sudah mengatur environtment variable dengan memasukkan redis, hanya tinggal di mengetik ```redis-cli``` di cmd
###### Library yang dibutuhkan : Tkinter, redis
###### Aplikasi ini belum sempurna masih banyak yang harus diperbaiki :)
