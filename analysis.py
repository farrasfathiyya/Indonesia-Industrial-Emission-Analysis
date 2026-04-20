import pandas as pd
import folium

# 1. read data
df = pd.read_csv('emisi_cilegon.csv')

# 2. Make the Cilegon city map
peta = folium.Map(location=[-6.01, 106.02], zoom_start=12, tiles='CartoDB positron')

# 3. Add an industrial location point to the map
for index, baris in df.iterrows():
    folium.Marker(
        location=[baris['lat'], baris['lon']],
        popup=f"{baris['nama_industri']} (Sektor: {baris['sektor']})",
        icon=folium.Icon(color='green', icon='industry', prefix='fa')
    ).add_to(peta)

# 4. Save the file result of the map
peta.save('peta_emisi_cilegon.html')
print("Done! Check the file 'peta_emisi_cilegon.html'.")
