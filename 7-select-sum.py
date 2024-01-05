import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
#INSERT DATA KE TABEL
kursor.execute("SELECT SUM(jml_skrg) FROM FAUNA")
total_populasi = kursor.fetchone()[0]

print(f"Total populasi hewan langka saat ini: {total_populasi}")

koneksi.close()   