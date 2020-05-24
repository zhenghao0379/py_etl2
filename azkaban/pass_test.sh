echo "原始参数：$1 $2 $3 $4 $5"
py_val="$1 $2 $3 $4 $5"
echo "{'py_val':$py_val}" > $JOB_OUTPUT_PROP_FILE
echo "{'py_val2':$py_val}" > $JOB_PROP_FILE