import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

#ubah berdasarkan id_pegawai
id_fauna = 10
jml_skrg_baru = 650

#Gunakan Query UPDATE SET 
kursor.execute(f"UPDATE FAUNA SET jml_skrg = {jml_skrg_baru} WHERE id_fauna = {id_fauna}")
koneksi.commit()

#cek apakahh data berhasil diubah atau belum 
if kursor.rowcount > 0: 
    print(f"Data Dengan ID {id_fauna} berhasil Diubah!")
else: 
    print(f"Tidak ada data pegawai dengan ID{id_fauna}!")

koneksi.close