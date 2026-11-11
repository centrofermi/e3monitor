# FC 2025/01/31

import geopandas as gpd
import matplotlib.pyplot as plt
import os
import matplotlib.colors as mcolors
from e3monitor.config.__files_server__ import pathSaveFig
# pathSaveFig = '/Users/fc/Downloads'

# Coordinates of the telescopes (example data)
telescopes = {
    'ALTA-01': (40.823349, 16.553749),
    'ANCO-01': (43.610184, 13.513950),
    'AREZ-01': (43.464649, 11.874017),
    'BARI-01': (41.119217, 16.871950),
    'BOLO-01': (44.8, 11.3+0.5),
    'BOLO-02': (44.8-0.2, 11.3+0.5),
    'BOLO-03': (44.8-0.4, 11.3+0.5),
    'BOLO-04': (44.8-0.6, 11.3+0.5),
    'BOLO-05': (44.8-0.8, 11.3+0.5),
    'CAGL-01': (39.23, 9.118067),
    'CAGL-02': (39.23-0.2, 9.123917),
    'CAGL-03': (39.23-0.4, 9.120600),
    'CARI-01': (39.489349, 16.956249),
    'CATA-01': (37.525032, 15.071700),
    'CATZ-01': (38.830666, 16.637234),
    'CERN-01': (46.229649, 6.051617),
    'CERN-02': (46.229568-0.2, 6.051383),
    'COSE-01': (39.310902, 16.254734),
    'FERM-01': (40.976959, 14.189270),
    'FRAS-01': (41.55, 12.664733),
    'FRAS-02': (41.55-0.2, 12.677450),
    'FRAS-03': (41.55-0.4, 12.671400),
    'GENO-01': (44.45, 8.971983),
    'GROS-01': (42.753468, 11.117650),
    'GROS-02': (42.749935, 11.118850),
    'LAQU-01': (42.356682, 13.414033),
    'LAQU-02': (42.355034, 13.413417),
    'LECC-01': (40.35, 18.192333),
    'LECC-02': (40.35-0.2, 18.166317),
    'LNLE-01': (45.351715, 11.948800),
    'LODI-01': (45.303883+0.2, 9.500150),
    'LODI-02': (45.303883, 9.498116),
    'LODI-03': (45.303883-0.2, 9.499033),
    'PARM-01': (44.800568, 10.320383),
    'PATE-01': (37.7, 14.901716),
    'PISA-01': (43.720463, 10.407999),
    'REGG-01': (44.705215, 10.634550),
    'ROMA-01': (41.898251, 12.5),
    'ROMA-02': (41.898251-0.2, 12.5),
    'SALE-01': (40.685017, 14.769250),
    'SALE-02': (40.685017-0.2, 14.765333),
    'SAVO-01': (44.3, 8.482917),
    'SAVO-02': (44.3-0.2, 8.478184),
    'SIEN-01': (43.326351, 11.316317),
    'SIEN-02': (43.324173, 11.321925),
    'TERA-01': (42.663799, 13.712100),
    'TORI-03': (45.063850, 7.662433),
    'TORI-04': (45.063850+0.2, 7.676100),
    'TRAP-01': (38.017982, 12.512733),
    'TREV-01': (45.668201, 12.237467),
    'TRIN-01': (41.352783, 16.096233),
    'VIAR-01': (43.871017, 10.244133),
    'VIAR-02': (43.871017+0.2, 10.244783),
    'VICE-01': (45.558201, 11.533366),
    'LAMP-01': (35.5025, 12.5747),  # Corrected coordinates for Lampedusa
}

# Load the map of Italy
italy = gpd.read_file("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_0_countries.geojson")
italy = italy[italy['ADMIN'] == "Italy"]

# Load the map of Italian regions
regions = gpd.read_file("https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson")

# Create a plot
fig, ax = plt.subplots(figsize=(25 , 25))
italy.plot(ax=ax, color='lightblue', edgecolor='white')

# Define a custom colormap with 4 shades of blue
# blues = mcolors.LinearSegmentedColormap.from_list("custom_blues", 
# ["#fbf8cc","#fde4cf","#ffcfd2","#f1c0e8","#cfbaf0","#a3c4f3","#90dbf4","#8eecf5","#98f5e1","#b9fbc0"],
#  N=10)
blues = mcolors.LinearSegmentedColormap.from_list("custom_blues", ["#00aaff", "#00aaff"], N=2)

# Plot the regions with the custom blue colormap
regions.plot(ax=ax, column='reg_name', cmap=blues, legend=False, edgecolor='white')

# Plot the telescopes
for name, (lat, lon) in telescopes.items():
    plt.plot(lon, lat, marker='o', color='green', markersize=12)
    plt.text(lon + 0.1, lat, name, fontsize=12, ha='left', color='black', fontweight='bold')

plt.title('Map of Italy with Telescopes and Regions', fontsize=20)
plt.xlabel('Longitude', fontsize=15)
plt.ylabel('Latitude', fontsize=15)
plt.grid(which='both', linestyle='--', linewidth=0.5, color='gray')

# Set the background color to green
ax.set_facecolor('#e0f7fa')

# Save the plot
output_path = os.path.join(pathSaveFig, 'map_italy_telescopes.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Plot saved to {output_path}")
