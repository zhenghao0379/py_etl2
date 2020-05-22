# 定位到工作根目录
# import sys
# from os.path import abspath, join, dirname
# sys.path.insert(0, join(abspath(dirname(__file__)), '../../'))
import os
import sys
sys.path.append(os.getcwd())

# 载入工具包和自定义工具包
import numpy as np
import pandas as pd

from package import *

# 获取连接
dev()
conn, engine = mysql_on("sakila")

# 获取数据
df_address = pd.read_sql("select * from address", engine).drop(['last_update'],axis=1)
df_city = pd.read_sql("select * from city", engine).drop(['last_update'],axis=1)
df_country = pd.read_sql("select * from country", engine).drop(['last_update'],axis=1)

# 数据处理
df_address["location_text"] = df_address["location"]
df_address["lat"] = df_address["location_text"]
df_address["lng"] = df_address["location_text"]

df_data = df_address.merge(df_city, how="left", on="city_id")
df_data_2 = df_data.merge(df_country, how="left", on="country_id")


lng_list = data_all["lng"].values.to_list
lat_list = data_all["lat"].values.to_list

map_list = map(get_address_api, lng_list, lat_list)

a = list(map_list)

df_data_2["address"] = a

df_data_2["省"] = df_data_2['a'][]
df_data_2["市"] = df_data_2['a'][]
df_data_2["区"] = df_data_2['a'][]

# 载入数据
conn, engine = mysql_on("test")
mysql_upload(df_data_2,"dim_address",conn,engine,type="r")
