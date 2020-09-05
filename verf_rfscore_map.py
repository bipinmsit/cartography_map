import sys
import os
import shutil
import numpy as np
import pandas as pd
import geopandas as gpd
from pyproj import CRS
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
# import sqlalchemy
# import pymysql
from datetime import datetime
from datetime import date
from datetime import timedelta

args1 = sys.argv[1]
args2 = sys.argv[2]

print(args1)
print(args2)

path = "/home/nwp/wrf/pyscript/VERF/map/"
dir=args1+args2
map_dir = os.path.join(path, dir)
if os.path.exists(map_dir):
    shutil.rmtree(map_dir)
os.makedirs(map_dir)
rf_path=map_dir
rf_dir="rf"
rf_map_dir = os.path.join(rf_path,rf_dir)
if os.path.exists(rf_map_dir):
    shutil.rmtree(rf_map_dir)
os.makedirs(rf_map_dir)
engine=sqlalchemy.create_engine('mysql+pymysql://root:rimes123@localhost:3306/imd_agro_database_final')
connection = engine.connect()

rf_score='select * from fc_verf_state_skill where month="'+str(args1)+'" and year="'+str(args2)+'"'
rf_score=pd.read_sql_query(rf_score,engine)
rs=rf_score[['state_id','day','ratio_score']]
hk=rf_score[['state_id','day','hk']]
pod=rf_score[['state_id','day','pod']]
far=rf_score[['state_id','day','far']]
shp = gpd.read_file("/home/nwp/agdss/scripts/st_shp_dd/st_shp_dd.shp")
df1 = shp.rename(columns={"ST_NM": "state_name", "Cen_ST_ID": "state_id"})
days = list(rf_score["day"])
days_list = list(dict.fromkeys(days))
#print(days_list)
for day in days_list:
    df2 = rs.loc[rf_score["day"] == day]
    new_df = pd.merge(df1, df2, on="state_id", how="left")
    new_df1=new_df.dropna()
    cmap = ListedColormap(["red", "orange", "blue", "green"])
    fig, ax = plt.subplots(figsize=(3,3))
    new_df1.plot(
    ax=ax,
    column=new_df1["ratio_score"],
    linewidth=0.5,
    cmap=cmap,   
    scheme='User_Defined',
    edgecolor='black',
    alpha=0.3,
    classification_kwds=dict(bins=[(25),50,75,100]),   
    legend=True,
    legend_kwds = {'fontsize':5,'loc':'upper right', 'markerscale':.3}
    )    
    # Add title
    ax.set_title('Ratio Score(Day-'+str(day)+')', fontdict={'fontsize': 5, 'fontweight': 'medium'})
    ax.tick_params(labelsize=5)
    plt.tight_layout()
    plt.savefig(rf_map_dir+"/RS_STT_D{}_{}_{}.png".format(day,args1,args2), dpi=300)


print("SUCESSFULLY RS MAP GENERATED")
#=================================================================================================================#

for day in days_list:
    df2 = hk.loc[rf_score["day"] == day]
    new_df = pd.merge(df1, df2, on="state_id", how="left")
    new_df1=new_df.dropna()
    cmap = ListedColormap(["red", "orange", "blue", "green"])
    fig, ax = plt.subplots(figsize=(3,3))
    new_df1.plot(
    ax=ax,
    column=new_df1["hk"],
    linewidth=0.5,
    cmap=cmap,
    scheme='User_Defined',
    edgecolor='black',
    alpha=0.3,
    classification_kwds=dict(bins=[0,0.20,0.25,0.5]),
    legend=True,
    legend_kwds = {'fontsize':5, 'loc':'upper right', 'markerscale':.3}
    )
    # Add title
    ax.set_title('HK Score(Day-'+str(day)+')', fontdict={'fontsize': 5, 'fontweight': 'medium'})
    ax.tick_params(labelsize=5)
    plt.tight_layout()
    plt.savefig(rf_map_dir+"/HK_STT_D{}_{}_{}.png".format(day,args1,args2), dpi=300)


print("SUCESSFULLY HK  MAP GENERATED")
#=================================================================================================================#

for day in days_list:
    df2 = pod.loc[rf_score["day"] == day]
    new_df = pd.merge(df1, df2, on="state_id", how="left")
    new_df1=new_df.dropna()
    cmap = ListedColormap(["red", "orange", "blue", "green"])
    fig, ax = plt.subplots(figsize=(3,3))
    new_df1.plot(
    ax=ax,
    column=new_df1["pod"],
    linewidth=0.5,
    cmap=cmap,
    scheme='User_Defined',
    edgecolor='black',
    alpha=0.3,
    classification_kwds=dict(bins=[25,50,75,100]),
    legend=True,
    legend_kwds = {'fontsize':5, 'loc':'upper right', 'markerscale':.3}
    )
    # Add title
    ax.set_title('POD (Day-'+str(day)+')', fontdict={'fontsize': 5, 'fontweight': 'medium'})
    ax.tick_params(labelsize=5)
    plt.tight_layout()
    plt.savefig(rf_map_dir+"/POD_STT_D{}_{}_{}.png".format(day,args1,args2), dpi=300)


print("SUCESSFULLY POD  MAP GENERATED")
#=================================================================================================================#
for day in days_list:
    df2 = far.loc[rf_score["day"] == day]
    new_df = pd.merge(df1, df2, on="state_id", how="left")
    new_df1=new_df.dropna()
    cmap = ListedColormap(["red", "orange", "blue", "green"])
    fig, ax = plt.subplots(figsize=(3,3))
    new_df1.plot(
    ax=ax,
    column=new_df1["far"],
    linewidth=0.5,
    cmap=cmap,
    scheme='User_Defined',
    edgecolor='black',
    alpha=0.3,
    classification_kwds=dict(bins=[25,50,75,100]),
    legend=True,
    legend_kwds = {'fontsize':5, 'loc':'upper right', 'markerscale':.3}
    )
    # Add title
    ax.set_title('FAR (Day-'+str(day)+')', fontdict={'fontsize': 5, 'fontweight': 'medium'})
    ax.tick_params(labelsize=5)
    plt.tight_layout()
    plt.savefig(rf_map_dir+"/FAR_STT_D{}_{}_{}.png".format(day,args1,args2), dpi=300)


print("SUCESSFULLY FAR  MAP GENERATED")
#=================================================================================================================#

