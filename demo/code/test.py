import sys
import os
sys.path.append(os.getcwd())

# import pandas as pd
# 全局变量 与 自定义函数
from package import *

table = ""

for day in DAYS:
    for rpt_type in RPT_TYPES:

        print(day)

        print(rpt_type)

        # sql = "select * from {table} where day = '{day}' and rpt_type='{RPT_TYPE}'"

        # data = pd.read_sql(sql, conn)

        # data.to_sql("film",conn,if_exists="append",index=False)

        # data.dtypes

        # data["last_update2"] = pd.to_datetime(data["last_update"], format='%Y-%m-%d %H:%m:%s')

    
