import pandas as pd
import geopandas as gpd
from pyproj import CRS
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import csv

# csv_file = pd.read_csv("./fc_verf_state_skill_may_stname.csv")
# shp = gpd.read_file("./st_shp/st_shp/st_shp.shp")
# df1 = shp.rename(columns={"ST_NM": "state_name", "Cen_ST_ID": "state_id"})

# fig, ax = plt.subplots(figsize=(12,8))
# df1.plot(ax=ax, linewidth=1, edgecolor='black', facecolor='none')

# # Add title
# ax.set_title("One day Rainfall")

# custom_lines = [Line2D([0], [0], color='black', linewidth=1)]
# ax.legend(custom_lines, ["  Indian States Boundaries"])

# plt.tight_layout()
# plt.savefig("test.png", dpi=300)

with open("./fc_verf_state_skill_july_rf.csv", "r", encoding='cp437') as filename:
    csv_read = csv.reader(filename)
    for row in csv_read:
        print(row)

