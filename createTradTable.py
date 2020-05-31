import sqlutil as ql
import tradingDayQuery as td
import datetime
import time

ql.conn.connect()

sql = 'select datelist from traddate2020;'
ql.cursor = ql.conn.cursor(cursor=ql.pymysql.cursors.DictCursor)

ql.cursor.execute(sql)
ret = ql.cursor.fetchall()
print(ret)

for i in ret:
    str_date = datetime.datetime.strftime(i['datelist'], '%Y-%m-%d')
    time.sleep(3)
    if td.is_tradeday(str_date) == 0:
        sql2 = 'update traddate2020 set istrad = %s where datelist = %s;'
        ql.cursor.execute(sql2, ['0', str_date])
        ql.conn.commit()
    else:
        sql3 = 'update traddate2020 set istrad = %s where datelist = %s;'
        ql.cursor.execute(sql3, ['1', str_date])
        ql.conn.commit()
    print(str_date + " commit successfully!")