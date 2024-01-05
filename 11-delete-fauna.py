import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

#Gunakan Query UPDATE SET 
kursor.execute(f"DELETE FROM FAUNA WHERE asal = 'Kalimantan' ")
koneksi.commit()

#cek apakahh data berhasil diubah atau belum 
if kursor.rowcount > 0: 
    print(f"Data Fauna berhasil Dihapus!")
else: 
    print(f"Tidak ada data Fauna!")

koneksi.close