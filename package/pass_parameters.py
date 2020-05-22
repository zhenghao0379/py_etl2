# 终端执行传递参数 apgparse
# 官方快速文档：https://docs.python.org/zh-cn/3/howto/argparse.html
# 官方详细文档：https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse
# 文档： https://pymotw.com/3/argparse/index.html#module-argparse

# 终端执行
# D:
# cd 

import argparse
import datetime

def get_DAYS(start, end):
    start = datetime.datetime.fromisoformat(start)
    end = datetime.datetime.fromisoformat(end)

    days = [start + datetime.timedelta(days=x) for x in range((end-start).days + 1)]
    days = [i.strftime("%F") for i in days]

    return days

PARSER = argparse.ArgumentParser(description='Short sample app')

PARSER.add_argument('-D', '--DAYS', help='运行日期，默认为昨天')
PARSER.add_argument('-S', '--START', help='起始日期，默认为昨天')
PARSER.add_argument('-E', '--END', help='终止日期，默认为昨天')
PARSER.add_argument('-T', '--RPT_TYPES', help='循环周期类型')
PARSER.add_argument('-M', '--MAIL', help='邮件接收者')

PARSER_ARGS = PARSER.parse_args()

yesterday = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%F")

if PARSER_ARGS.DAYS:
    DAYS = PARSER_ARGS.DAYS.split(',')
    START = min(DAYS)
    END = max(DAYS)
elif PARSER_ARGS.START and PARSER_ARGS.END:
    START = PARSER_ARGS.START
    END = PARSER_ARGS.END
elif PARSER_ARGS.START:
    START = PARSER_ARGS.START
    END = yesterday
    DAYS = get_DAYS(START, END)
else:
    DAYS = [yesterday]
    START = yesterday
    END = yesterday

if PARSER_ARGS.RPT_TYPES:
    RPT_TYPES = PARSER_ARGS.RPT_TYPES.split(',')
else:
    RPT_TYPES = ['D']

print('DAYS =', DAYS)
print('START =', START)
print('END =', END)
print('RPT_TYPES =', RPT_TYPES)
