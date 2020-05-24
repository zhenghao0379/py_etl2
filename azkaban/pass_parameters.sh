## 负责接收azkaban web 参数, 放在 commend: python3 test.py ${py_val}

# ('-S', '--START', help='起始日期，默认为昨天')
# ('-E', '--END', help='终止日期，默认为昨天')
# ('-D', '--DAYS', help='运行日期，默认为昨天')
# ('-T', '--RPT_TYPES', help='循环周期类型')
# ('-M', '--MAIL', help='邮件接收者')


# 原始参数
echo "原始参数：$1 $2 $3 $4 $5"

# 接收参数
if [ $1 != '${D}' ]
then
  DAYS = "-D $1"
else
  DAYS = ''
fi

if [ $2 != '${S}' ]
then
  START = "-S $2"
else
  START = ''
fi

if [ $3 != '${E}' ]
then
  END = "-E $3"
else
  END = ''
fi

if [ $4 != '${T}' ]
then
  RPT_TYPES = "-T $4"
else
  RPT_TYPES = ''
fi

if [ $5 != '${M}' ]
then
  MAIL = "-M $5"
else
  MAIL = ''
fi

echo "------输入参数------"
echo "DAYS:$DAYS"
echo "START:$START"
echo "END:$END"
echo "RPT_TYPES:$RPT_TYPES"
echo "MAIL:$MAIL"
echo "-------------------"

py_flow_val="$DAYS $START $END $RPT_TYPES $MAIL"

echo "{'py_flow_val': $py_flow_val}" > $JOB_OUTPUT_PROP_FILE