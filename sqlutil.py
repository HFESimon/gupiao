import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database='gupiao',
    charset='utf8'
)

# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 得到一个可以执行SQL语句并且将结果作为字典返回的光标对象
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 定义要执行的SQL语句(创建表结构)
# sql='select * from abc001;'
# cursor.execute(sql)
# ret = cursor.fetchall()  # 查看全部数据
#ret = cursor.fetchone()  # 查看单条数据
#ret = cursor.fetchmany(3)  # 指定数量查看
# print(ret)

cursor.close()
conn.close()
