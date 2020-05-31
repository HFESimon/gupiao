from decimal import Decimal

import sqlutil as ql
import datetime

ql.conn.connect()
ql.cursor = ql.conn.cursor(cursor=ql.pymysql.cursors.DictCursor)
sql = 'select date, max_price, min_price from abc007_defect;'
ql.cursor.execute(sql)
ret = ql.cursor.fetchall()
print(ret)

max_price_list = []
min_price_list = []
sum = 0
averagePrice = 0

for i in ret:
    max_price_list.append(i['max_price'])
    min_price_list.append(i['min_price'])

print(max_price_list)
print(min_price_list)

for x in range(len(max_price_list)):
    sum = sum + max_price_list[x]

for y in range(len(min_price_list)):
    sum = sum + min_price_list[y]

averagePrice = sum / (len(max_price_list) + len(min_price_list))
print(Decimal(averagePrice).quantize(Decimal('0.00')))