import os
import sys
sys.path.append(os.getcwd())

from package import *

table_name = 'ods_house'

print('hello world, hello python, hello azkaban')

for day in DAYS:
    for rpt_type in RPT_TYPES:
        print(day)
        print(rpt_type)

        sql_day = f"select * from {table_name} where day = {day}"
        print(sql_day)
        host = CONFIG.get_value('mysql', 'host')
        print('192.168.1.1')
        print(host)
        print(type(host))