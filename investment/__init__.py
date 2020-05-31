import datetime
import sqlutil as ql
import pyecharts.options as opts
from pyecharts.charts import Line
import matplotlib as plt

ql.conn.connect()
ql.cursor = ql.conn.cursor(cursor=ql.pymysql.cursors.DictCursor)
sql = ('''select date, start_price, stop_price from abc001_defect where DATE_FORMAT(date, '%Y-%m-%d') >= '2019-01-01' and DATE_FORMAT(date, '%Y-%m-%d') <= '2019-12-31';''')
ql.cursor.execute(sql)
ret = ql.cursor.fetchall()
print(ret)

price_difference = []
stop_price = []
str_date = []
daliy_rate = ['NONE']

for i in ret:
    str_date.append(datetime.datetime.strftime(i['date'], '%Y-%m-%d'))
    stop_price.append(i['stop_price'])
    price_difference.append(float(format(i['stop_price'] - i['start_price'], '.6f')))
print(str_date)

print(price_difference)
print(stop_price)

# 计算每日收益收益率返回每日收益率list
def fun(differencelist, stoplist, daliylist):
    for i in range(len(differencelist)):
        if i != 0:
            daliylist.append(float(format(differencelist[i - 1] / stoplist[i], '.6f')))
    return daliylist

daliy_rate = fun(price_difference, stop_price, daliy_rate)
print(daliy_rate)

# 年化收益率
sum = 0
for x in range(len(daliy_rate)):
    if x != 0:
        sum = sum + float(daliy_rate[x])
mu = sum / len(daliy_rate)
print(mu)
year_rate = (1 + mu)**len(ret) - 1
print("年化收益率：{}".format(year_rate))

# 日收益率图
x_data = str_date
y_data = daliy_rate
(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        is_smooth=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("abc001rateline.html")
)
