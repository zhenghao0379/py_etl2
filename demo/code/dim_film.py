# 定位到工作根目录
import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../../'))

# 载入工具包和自定义工具包
import numpy as np
import pandas as pd

from package.env import *
from package.source.sql_connect import *

# 获取连接
dev()
conn, engine = mysql_on("sakila")

# sql
df_film = pd.read_sql("select * from film", engine).drop(['last_update'],axis=1)
df_film_category = pd.read_sql("select * from film_category", engine).drop(['last_update'],axis=1)
df_category = pd.read_sql("select * from category", engine).drop(['last_update'],axis=1).rename(columns={"name":"category_name"})
df_language = pd.read_sql("select * from language", engine).drop(['last_update'],axis=1).rename(columns={"name":"language_name"})

# 
df_data = df_film.merge(df_film_category, how="left", on="film_id")
df_data_2 = df_data.merge(df_category, how="left", on="category_id")
df_data_3 = df_data_2.merge(df_language, how="left", on="language_id")

# 载入数据
conn, engine = mysql_on("test")
mysql_upload(df_data_3,"dim_film",conn,engine,type="r")
