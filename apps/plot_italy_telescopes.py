# FC 2025/01/31

import geopandas as gpd
import matplotlib.pyplot as plt
import os
import matplotlib.colors as mcolors
from e3monitor.config.__files_server__ import pathSaveFig
# pathSaveFig = '/Users/fc/Downloads'

# Coordinates of the telescopes (example data)
telescopes = {
    'ALTA-01': (45.0703, 7.6869),
    'AREZ-01': (43.4633, 11.8797),
    'BARI-01': (41.1171, 16.8719),
    'BOLO-01': (44.4949, 11.3426),
    'CAGL-01': (39.2238, 9.1217),
    'CARI-01': (41.9028, 12.4964),
    'CATA-01': (37.5079, 15.0830),
    'CATZ-01': (37.5079, 15.0830),
    'CERN-01': (46.2044, 6.1432),
    'COSE-01': (45.0703, 7.6869),
    'FRAS-01': (42.3426, 13.3995),
    'GROS-01': (42.7636, 11.1124),
    'GROT-01': (42.7636, 11.1124),
    'LAQU-01': (42.3499, 13.3995),
    'LECC-01': (45.8566, 9.3977),
    'LODI-01': (45.3142, 9.5037),
    'PISA-01': (43.7228, 10.4017),
    'PARM-01': (44.8015, 10.3279),
    'PATE-01': (40.6401, 15.8051),
    'REGG-01': (44.6983, 10.6312),
    'ROMA-01': (41.9028, 12.4964),
    'SALE-01': (44.8898, 8.2065),
    'SAVO-01': (44.8898, 8.2065),
    'TERA-01': (45.0703, 7.6869),
    'TORI-01': (45.0703, 7.6869),
    'TRAP-01': (38.0176, 12.5364),
    'TREV-01': (45.6669, 12.2425),
    'TRIN-01': (39.2238, 9.1217),
    'VIAR-01': (45.0703, 7.6869),
    'FRAS-03': (42.3426, 13.3995),
    'GROS-02': (42.7636, 11.1124),
    'SIEN-01': (43.3188, 11.3308),
    'VICE-01': (45.0703, 7.6869),
    'LODI-02': (45.3142, 9.5037),
    'SIEN-02': (43.3188, 11.3308),
    'LAMP-01': (35.5025, 12.5747),  # Corrected coordinates for Lampedusa
}

# Load the map of Italy
italy = gpd.read_file("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_0_countries.geojson")
italy = italy[italy['ADMIN'] == "Italy"]

# Load the map of Italian regions
regions = gpd.read_file("https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson")

# Create a plot
fig, ax = plt.subplots(figsize=(15, 15))
italy.plot(ax=ax, color='lightblue', edgecolor='black')

# Define a custom colormap with 4 shades of blue
blues = mcolors.LinearSegmentedColormap.from_list("custom_blues", 
["#fbf8cc","#fde4cf","#ffcfd2","#f1c0e8","#cfbaf0","#a3c4f3","#90dbf4","#8eecf5","#98f5e1","#b9fbc0"],
 N=10)

# Plot the regions with the custom blue colormap
regions.plot(ax=ax, column='reg_name', cmap=blues, legend=False, edgecolor='white')

# Plot the telescopes
for name, (lat, lon) in telescopes.items():
    plt.plot(lon, lat, marker='o', color='green', markersize=8)
    plt.text(lon, lat, name, fontsize=12, ha='right', color='black')

plt.title('Map of Italy with Telescopes and Regions', fontsize=20)
plt.xlabel('Longitude', fontsize=15)
plt.ylabel('Latitude', fontsize=15)
plt.grid(True)

# Save the plot
output_path = os.path.join(pathSaveFig, 'map_italy_telescopes.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Plot saved to {output_path}")
