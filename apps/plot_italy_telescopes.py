# FC 2025/01/31

import geopandas as gpd
import matplotlib.pyplot as plt
from e3monitor.config.__files_server__ import (pathSaveFig)

# Coordinates of the telescopes (example data)
telescopes = {
    'ALTA-01': (45.0703, 7.6869),
    'AREZ-01': (43.4633, 11.8797),
    'BARI-01': (41.1171, 16.8719),
    'BOLO-01': (44.4949, 11.3426),
    'BOLO-02': (44.4949, 11.3426),
    'BOLO-03': (44.4949, 11.3426),
    'BOLO-04': (44.4949, 11.3426),
    'BOLO-05': (44.4949, 11.3426),
    'CAGL-01': (39.2238, 9.1217),
    'CAGL-02': (39.2238, 9.1217),
    'CAGL-03': (39.2238, 9.1217),
    'CAGL-04': (39.2238, 9.1217),
    'CARI-01': (41.9028, 12.4964),
    'CATA-01': (37.5079, 15.0830),
    'CATA-02': (37.5079, 15.0830),
    'CATZ-01': (37.5079, 15.0830),
    'CERN-01': (46.2044, 6.1432),
    'CERN-02': (46.2044, 6.1432),
    'COSE-01': (45.0703, 7.6869),
    'FRAS-01': (42.3426, 13.3995),
    'FRAS-02': (42.3426, 13.3995),
    'GROS-01': (42.7636, 11.1124),
    'GROT-01': (42.7636, 11.1124),
    'LAQU-01': (42.3499, 13.3995),
    'LAQU-02': (42.3499, 13.3995),
    'LECC-01': (45.8566, 9.3977),
    'LECC-02': (45.8566, 9.3977),
    'LECC-03': (45.8566, 9.3977),
    'LODI-01': (45.3142, 9.5037),
    'PISA-01': (43.7228, 10.4017),
    'PARM-01': (44.8015, 10.3279),
    'PATE-01': (40.6401, 15.8051),
    'REGG-01': (44.6983, 10.6312),
    'ROMA-01': (41.9028, 12.4964),
    'ROMA-02': (41.9028, 12.4964),
    'SALE-01': (44.8898, 8.2065),
    'SALE-02': (44.8898, 8.2065),
    'SAVO-01': (44.8898, 8.2065),
    'SAVO-02': (44.8898, 8.2065),
    'SAVO-03': (44.8898, 8.2065),
    'TERA-01': (45.0703, 7.6869),
    'TORI-01': (45.0703, 7.6869),
    'TORI-02': (45.0703, 7.6869),
    'TORI-03': (45.0703, 7.6869),
    'TORI-04': (45.0703, 7.6869),
    'TRAP-01': (38.0176, 12.5364),
    'TREV-01': (45.6669, 12.2425),
    'TRIN-01': (39.2238, 9.1217),
    'VIAR-01': (45.0703, 7.6869),
    'VIAR-02': (45.0703, 7.6869),
    'FRAS-03': (42.3426, 13.3995),
    'GROS-02': (42.7636, 11.1124),
    'SIEN-01': (43.3188, 11.3308),
    'VICE-01': (45.0703, 7.6869),
    'LODI-02': (45.3142, 9.5037),
    'SIEN-02': (43.3188, 11.3308),
    'LAMP-01': (45.0703, 7.6869),
    'POLA-01': (45.0703, 7.6869),
    'POLA-02': (45.0703, 7.6869),
}

# Load the map of Italy
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
italy = world[(world.name == "Italy")]

# Create a plot
fig, ax = plt.subplots(figsize=(10, 10))
italy.plot(ax=ax, color='white', edgecolor='black')

# Plot the telescopes
for name, (lat, lon) in telescopes.items():
    plt.plot(lon, lat, marker='o', color='red', markersize=5)
    plt.text(lon, lat, name, fontsize=9, ha='right')

plt.title('Map of Italy with Telescopes')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.savefig(pathSaveFig + '/italy_telescopes.png')