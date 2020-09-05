import pandas as pd
import geopandas as gpd
from pyproj import CRS
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

csv_file = pd.read_csv("./fc_verf_state_skill_july_rf.csv")
shp = gpd.read_file("./st_shp/st_shp/st_shp.shp")
df1 = shp.rename(columns={"ST_NM": "state_name", "Cen_ST_ID": "state_id"})
days = list(csv_file["day"])
days_list = list(dict.fromkeys(days))
for day in days_list:
    df2 = csv_file[["state_id", "state_name", "rs"]].loc[csv_file["day"] == day]
    new_df = pd.merge(df1, df2, on="state_id", how="left")
    
    cmap = ListedColormap(["red", "orange", "blue", "green"])

    fig, ax = plt.subplots(figsize=(3,3))
    df1.plot(ax=ax, linewidth=1, color='black')

    new_df.plot(
    ax=ax,
    column=new_df["rs"],
    linewidth=1,
    cmap=cmap,
    scheme='User_Defined',
    edgecolor='black',
    alpha=0.9,
    classification_kwds=dict(bins=[40, 60, 80, 100]),
    legend=True,
    legend_kwds = {'fontsize':5, 'loc':'upper right', 'markerscale':.3}
    )
    
    # Add title
    ax.set_title("One day Rainfall", size=5)
    ax.tick_params(labelsize=5)  
    plt.tight_layout()
    plt.savefig("day_{}.png".format(day), dpi=300)

