# 定位到工作根目录
import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../../'))

# 载入工具包和自定义工具包
import numpy as np
import pandas as pd

from package.env import *
from package.source.sql_connect import *

dev()
conn, engine = mysql_on("sakila")
test()
conn1, engine1 = mysql_on("test")

# for day in DAYS:
day = '2019-12-20'
df_rental = pd.read_sql("select * from rental".format_map(vars()), engine).drop(['last_update'],axis=1).rename(columns={'staff_id':'staff_id_rental'})
df_inventory = pd.read_sql("select * from inventory", engine).drop(['last_update'],axis=1)
df_payment = pd.read_sql("select * from payment", engine).drop(['customer_id','last_update'],axis=1).rename(columns={'staff_id':'staff_id_payment'})

df_data = df_rental.merge(df_inventory, how="left", on="inventory_id")
df_data2 = df_data.merge(df_payment, how="left", on="rental_id")

mysql_upload(df_data2, "mid_rental", conn1, engine1, type="r")

mysql_close(conn, engine)
mysql_close(conn1, engine1)
