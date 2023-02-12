# -*- coding: utf-8 -*-

# Install & import library prettytable untuk membuat tabel
!pip install prettytable
from prettytable import PrettyTable

# Membuat Class Transaction untuk menangani transaksi customer (terdiri dari banyak method)
class Transaction:

    # Method yang menginisialisasi "items" dalam bentuk dictionary yang digunakan menyimpan item yang dibeli
    def __init__(self):
        self.items = {}
    
    """ 
    Method untuk menambah item baru yang mengambil input dari customer seperti 
    nama item, jumlah (int), dan harga (int). Lalu membuat dictionary baru dengan 
    key value "name" dan menampilkan pesan, item sudah ditambahkan.
    """
    def add_item(self):
        name = input("Masukkan nama item: ")
        while True:
          try:
              qty = int(input("Masukkan jumlah: "))
              break
          except ValueError:
            print("Please input a number for quantity.")
        while True:
          try:
             price = int(input("Masukkan harga: "))
             break
          except ValueError:
            print("Please input a number for price.")
        item = {"name": name, "quantity": qty, "price": price}
        self.items[name] = item
        print(f"Item {name} dengan jumlah {qty} & harga {price} telah ditambahkan.")
        
    """
    Method menghapus item dari transaksi yang mengambil dari input customer sebagai 
    nama item yang ingin dihapus. Jika nama item ditemukan di dalam dictionary items,
    maka item tersebut akan dihapus.
    """
    def remove_item(self):
        name = str(input("Masukkan nama item yang ingin dihapus: "))
        if name in self.items:
            self.items.pop(name)
            print(f"Item {name} telah dihapus.")
        else:
            print(f"Item {name} tidak ditemukan.")  

    """
    Method update nama item yang sudah ada di dalam transaksi yang mengambil input dari
    customer sebagai nama item yang ingin diupdate dan nama baru yang ingin digunakan.
    Jika nama item ditemukan, maka nama item tersebut akan diupdate.
    """  
    def update_name(self):
        name = str(input("Masukkan nama item yang ingin diupdate: "))
        new_name = str(input("Masukkan nama baru: "))
        if name in self.items:
            item = self.items[name]
            item["name"] = new_name
            print(f"Nama item {name} telah diupdate menjadi {new_name}.")
        else:
            print(f"Item {name} tidak ditemukan.")
          
    """
    Method update harga item yang sudah ada di dalam transaksi yang mengambil input dari
    customer sebagai nama item yang ingin diupdate dan harga baru yang ingin digunakan.
    Jika nama item ditemukan, maka harga item tersebut akan diupdate.
    """  
    def update_price(self):
        name = str(input("Masukkan nama item yang ingin diupdate: "))
        new_price = int(input("Masukkan harga baru: "))
        if name in self.items:
            item = self.items[name]
            item["price"] = new_price
            print(f"Harga item {name} telah diupdate menjadi {new_price}.")
        else:
            print(f"Item {name} tidak ditemukan.")

    """
    Method update jumlah item yang sudah ada di dalam transaksi yang mengambil input dari
    customer sebagai nama item yang ingin diupdate dan jumlah terbaru yang ingin digunakan.
    Jika nama item ditemukan, maka jumlah item tersebut akan diupdate.
    """     
    def update_qty(self):
        name = str(input("Masukkan nama item yang ingin diupdate: "))
        new_qty = int(input("Masukkan jumlah yang baru: "))
        if name in self.items:
            item = self.items[name]
            item["quantity"] = new_qty
            print(f"Jumlah item {name} telah diupdate menjadi {new_qty}.")
        else:
            print(f"Item {name} tidak ditemukan.")

    # Method untuk menghapus semua atau mereset transaksi menjadi kosong
    def reset_transaction(self):
        self.items.clear()
        print("Transaksi telah direset.")

    # Method untuk menghitung total harga/item
    def total_harga(self, qty, price):
        return qty * price

    """
     Method untuk memeriksa apakah pesanan yang dimasukkan oleh user valid atau tidak. 
     Tidak valid jika jumlah item atau harga item < 0.
     Kemudian menampilkan tabel dari semua pesanan customer.
    """
    def check_order(self):
        if self.items:
          is_valid = True
          for item in self.items.values():
           if item["quantity"] < 0 or item["price"] < 0:
              #print(f"Pesanan yang anda masukan salah")
              is_valid = False
              break
          if not is_valid:
            print(f"Pesanan yang anda masukan salah")
          else:
            print (f"Pesananan yang anda masukan sudah benar")
            print (" " * 14,"Daftar Pesanan")
          table = PrettyTable()
          table.field_names = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
          nomer = 1
          for item in self.items.values():
            total = self.total_harga(item["quantity"], item["price"])
            table.add_row([nomer, item["name"], item["quantity"], item["price"], total])
            nomer += 1
          print(table)
        else:
             print("Tidak ada order.")

    """
    Method untuk menghitung total harga seluruh transaksi pesanan customer. 
    Jika total harga kurang dari 200.000, maka akan ditampilkan hanya total harga .
    Jika total harga lebih dari 200.000, maka akan diberikan diskon:
      - 5% jika total harga diantara 200.000 - 300.000
      - 8% jika total harga di antara 300.000 - 500.000
      - 10% jika total harga lebih dari 500.000.
    """
    def total_price(self):
        if self.items:
          total_semua = sum(item["quantity"]*item["price"] for item in self.items.values())

        table = PrettyTable()
        table.field_names = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        nomer = 1
        for item in self.items.values():
            total = self.total_harga(item["quantity"], item["price"])
            table.add_row([nomer, item["name"], item["quantity"], item["price"], total])
            nomer += 1
        print("Daftar Pesanan")
        print(table)
  
        if total_semua < 200_000:
           print(f"Total harga seluruh transaksi: {total_semua}")
        elif total_semua >= 200_001 and total_semua < 300_000:
            diskon = total_semua * 0.05 
            after_diskon = total_semua - diskon
            print(f"Total harga seluruh transaksi: {total_semua}")
            print(f"Selamat! Anda Mendapatkan diskon 5% sebesar {diskon}")
            print(f"Total harga yang dibayar {after_diskon}")
        elif total_semua >= 300_001 and total_semua < 500_000:
             diskon = total_semua * 0.08
             after_diskon = total_semua - diskon
             print(f"Total harga seluruh transaksi: {total_semua}")
             print(f"Selamat! Anda Mendapatkan diskon 8% sebesar {diskon}")
             print(f"Total harga yang dibayar {after_diskon}")
        else:
            total_semua > 500_000
            diskon = total_semua * 0.1
            after_diskon = total_semua - diskon
            print(f"Total harga seluruh transaksi: {total_semua}")
            print(f"Selamat! Anda Mendapatkan diskon 10% sebesar {diskon}")
            print(f"Total harga yang dibayar {after_diskon}")

# Menginisialisasi class Kasir yang memanggil class Transction
class Kasir(Transaction):

      # Method init yang menjalankan class yang di-extend (Transaction) dan menginisialisasi 
      # objek dari class Transaction yang diberi nama trnsct_123 
      def __init__(self):
         super().__init__()
         self.trnsct_123 = Transaction()

      """
      Method menampilkan menu utama aplikasi kasir. 
      Pada menu tersebut terdapat 9 pilihan seperti tambah pesanan, periksa pesanan, 
      update nama pesanan dan sebagainya. Saat user memasukkan pilihannya, 
      program akan mengeksekusi perintah sesuai dengan pilihan yang dipilih. 
      """
      def main_menu(self):
          lanjut_beli = "y"
          while lanjut_beli == "y" or lanjut_beli == "Y":
            print("\n")
            print('=' * 10, 'MAIN MENU APLIKASI KASIR', '=' * 10)
            print(' ' * 5,'Selamat Datang di Toko PaccMaret',)
            print('1. Tambah pesanan')
            print('2. Periksa pesanan')
            print('3. Update nama pesanan')
            print('4. Update jumlah pesanan')
            print('5. Update harga pesanan')
            print('6. Hapus pesanan')
            print('7. Reset pesanan')
            print('8. Total harga keseluruhan pesanan')
            print('9. Keluar')

            """
            Memeriksa apakah input yang diterima berada dalam rentang 1-9. Jika tidak, 
            maka akan terdapat error ValueError. Silakan masukkan angka 1-9." akan ditampilkan. 
            Kemudian perintah "continue", program akan kembali ke awal dan mengulang proses input.
            """
          # input pilihan
            try:
                pilihan = int(input('Pilih menu: '))
                if pilihan not in range(1, 10):
                    raise ValueError
            except ValueError:
                print("Pilihan tidak valid. Silakan masukkan angka 1-9.")
                continue
          

          # pilihan menu & method yang akan dipanggil
            if pilihan == 1:
              self.trnsct_123.add_item()
            elif pilihan == 2:
              self.trnsct_123.check_order()
            elif pilihan == 3:
              self.trnsct_123.update_name()
            elif pilihan == 4:
              self.trnsct_123.update_qty()
            elif pilihan == 5:
              self.trnsct_123.update_price()
            elif pilihan == 6:
              self.trnsct_123.remove_item()
            elif pilihan == 7:
              self.trnsct_123.reset_transaction()
            elif pilihan == 8:
              self.trnsct_123.total_price()
              lanjut_beli = input("Ingin membeli lagi? <y/n> ")
              if lanjut_beli == "n" or lanjut_beli == "N":
                print("Terima kasih sudah mengunjungi PaccMaret")
                break
            else:
              print("keluar aplikasi. Terima kasih telah mengunjungi PaccMaret")
              break

"""Membuat instance kasir_1 dari class Kasir. Kita dapat memanggil 
metode-metode pada kelas Kasir melalui instance kasir_1"""
kasir_1 = Kasir()

# Memanggil metode main_menu melalui kasir_1 dari kelas Kasir
kasir_1.main_menu()
