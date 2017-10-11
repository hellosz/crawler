#-*-encoding=utf8-*-
import re
startUrl = 'http://www.jikexueyuan.com/course/?pageNum=2'
res = re.search('pageNum=(\d+)', startUrl, re.S)
print(res)