import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

#Gunakan Query UPDATE SET 
kursor.execute(f"UPDATE FAUNA SET asal = 'Kalimantan Timur' WHERE nama_fauna = 'Katak Borneo'")
koneksi.commit()

#cek apakahh data berhasil diubah atau belum 
if kursor.rowcount > 0: 
    print(f"Data fauna berhasil Diubah!")
else: 
    print(f"Tidak ada data fauna!")

koneksi.close