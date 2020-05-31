import sqlutil as ql
import tradingDayQuery as td
import datetime
import time

ql.conn.connect()

# sql1='insert into abc001_defect(date) select datelist from calendar where DATE_FORMAT(datelist, '%Y-%m-%d') >= '2019-01-29' and DATE_FORMAT(datelist, '%Y-%m-%d') <= '2020-03-26';' 插入日期数据
sql2 = 'select t.date, d.istrad from abc010_defect t, traddate d where t.date=d.date;'
# sql3 = 'update
#     abc001_defect t, abc001 b
# set
#     t.start_price=b.start_price,t.max_price=b.max_price,t.min_price=b.min_price,t.stop_price=b.stop_price,t.num=b.num
# where
#     t.date=b.date;' 迁移数据
ql.cursor = ql.conn.cursor(cursor=ql.pymysql.cursors.DictCursor)

ql.cursor.execute(sql2)
ret = ql.cursor.fetchall()  # 查看全部数据
print(ret)

for i in ret:
    str_date = datetime.datetime.strftime(i['date'], '%Y-%m-%d')
    if i['istrad'] == 0:
        sql3 = 'delete from abc010_defect where date = %s;'
        ql.cursor.execute(sql3, [str_date])
        ql.conn.commit()
    print(str_date + " commit successfully!")


# sql = 'insert into abc001_defect(date) values(%s);'


ql.cursor.close()
ql.conn.close()