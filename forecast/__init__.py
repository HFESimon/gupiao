import sqlutil as ql
import tradingDayQuery as td
import datetime
import time
import random

ql.conn.connect()

sql = 'select * from abc001_defect2020;'
ql.cursor = ql.conn.cursor(cursor=ql.pymysql.cursors.DictCursor)
sql2 = 'select t.date, d.istrad from abc001_defect2020 t, traddate d where t.date=d.date;'
sql3 = 'select datelist from traddate2020 where istrad = 0;'
sql5 = '''select date from abc010_defect2020 where DATE_FORMAT(date, '%Y-%m-%d') > '2020-03-26';'''

ql.cursor.execute(sql)
ret = ql.cursor.fetchall()
ql.cursor.execute(sql2)
ret2 = ql.cursor.fetchall()
ql.cursor.execute(sql3)
ret3 = ql.cursor.fetchall()

# 删非交易日字段
# for i in ret3:
#     str_date = datetime.datetime.strftime(i['datelist'], '%Y-%m-%d')
#     sql4 = 'delete from abc001_defect2020 where date = %s;'
#     ql.cursor.execute(sql4, [str_date])
#     ql.conn.commit()

ql.cursor.execute(sql5)
ret4 = ql.cursor.fetchall()
date_list = []
for i in ret4:
    date_list.append(datetime.datetime.strftime(i['date'], '%Y-%m-%d'))

print(date_list)
kuadu = 4
jichu = 4.5

for i in range(len(date_list)):
    sql6 = '''update abc010_defect2020 set start_price=%s, max_price=%s, min_price=%s, stop_price=%s, num=%s  where date = %s;'''
    s_p = jichu + round(random.uniform(0, kuadu), 3)
    max_p = (jichu+1) + round(random.uniform(0, kuadu), 3)
    min_p = (jichu-1) + round(random.uniform(0, kuadu), 3)
    stop_p = jichu + round(random.uniform(0, kuadu), 3)
    num = random.randint(800000, 8000000)
    data = [s_p, max_p, min_p, stop_p, num, date_list[i]]
    ql.cursor.execute(sql6, data)
    ql.conn.commit()
