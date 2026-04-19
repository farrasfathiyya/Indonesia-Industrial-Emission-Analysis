import pandas as pd
import folium

# 1. Membaca data dari file yang kamu ganti namanya tadi
df = pd.read_csv('emisi_cilegon.csv')

# 2. Membuat peta pusat kota Cilegon
peta = folium.Map(location=[-6.01, 106.02], zoom_start=12, tiles='CartoDB positron')

# 3. Menambahkan titik lokasi industri ke peta
for index, baris in df.iterrows():
    folium.Marker(
        location=[baris['lat'], baris['lon']],
        popup=f"{baris['nama_industri']} (Sektor: {baris['sektor']})",
        icon=folium.Icon(color='green', icon='industry', prefix='fa')
    ).add_to(peta)

# 4. Simpan hasilnya jadi file peta
peta.save('peta_emisi_cilegon.html')
print("Selesai! Cek file 'peta_emisi_cilegon.html' di foldermu.")
