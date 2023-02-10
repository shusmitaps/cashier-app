# cashier-app
Cashier Application sederhana dengan bahasa Python untuk Pacmann Project

# Latar Belakang
Seorang pemilik supermatket besar disalah satu kota di Indonesia memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu ingin membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukan item yang dibeli, jumlah item yang dibeli dan harga item yang dibeli.

# Requirements / Objective
- Membuat sistem kasir yang self-service di supermarket sehingga memudahkan customer dalam bertransaksi
- Customer dapat memasukan nama item, jumlah item dan harga barang
- Jika ada kesalahan, tetapi tidak ingin menghapus itemnya, customer bisa update item atau update jumlah item dan atau update harga item
- Jika batal membeli item belanjaan, customer bisa menghapus salah satu item dari nama item atau langsung menghapus semua transaksi atau reset transaksi
- Ketika sudah selesai belanja, customer bisa melakukan check order untuk memeriksa pesanan yang di masukan sudah benar atau belum
- Customer dapat menghitung total belanja yang sudah dipesan, kemudian terdapat ketentuan sebagai berikut :
    - Jika total belanja di atas Rp 200.000 maka akan mendapatkan diskon 5%
    - Jika total belanja di atas Rp 300.000 maka akan mendapatkan diskon 8%
    - Jika total belanja di atas Rp 500.000 maka akan mendapatkan diskon 10%
   
# Flowcart
![Logo](https://github.com/ura-mita/cashier-app/blob/main/pictures/flowchart%20cashier%20app.png)

# Function dan Atribut
- ```Self.items``` : Atribut yang berupa dictionary yang berfungsi untuk menyimpan data transaksi yang dilakukan oleh customer
- ```add_item``` : Method yang berfungsi untuk menambahkan list produk yang telah dimasukkan oleh customer yang berisi nama item, jumlah item, dan harga item
- ```update_name``` : Method yang berguna untuk mengubah nama item yang ingin diganti
- ```update_qty``` : Method yang berguna untuk mengubah jumlah item yang di-order
- ```update_price``` : Method yang berfungsi untuk mengubah harga item yang dibeli
- ```remove_item``` : Method yang digunakan untuk menghapus item tertentu
- ```reset_transaction``` : Method yang digunakan untuk menghapus seluruh data transaksi
- ```check_order``` : Method yang berfungsi untuk menampilkan seluruh data transaksi yang telah dibuat
- ```total_harga``` : Method untuk menghitung total harga/item
- ```total_price``` : Method yang digunakan untuk menampilkan total harga seluruh produk
- ```Main_menu``` : Method menampilkan menu utama aplikasi kasir. Pada menu tersebut terdapat 9 pilihan seperti tambah pesanan, periksa pesanan, update nama pesanan dan sebagainya. Saat user memasukkan pilihannya, program akan mengeksekusi perintah sesuai dengan pilihan yang dipilih. 
