from pyecharts import options as opts
from pyecharts.charts import Kline
import sqlutil as ql
import datetime

ql.conn.connect()
ql.cursor = ql.conn.cursor(cursor=ql.pymysql.cursors.DictCursor)
sql = 'select date, start_price, max_price, min_price, stop_price from abc003_defect;'
ql.cursor.execute(sql)
ret = ql.cursor.fetchall()
print(ret)

x_data = []
y_data = []

for i in ret:
    str_date = datetime.datetime.strftime(i['date'], '%Y-%m-%d')
    x_data.append(str_date)
    y_data.append([i['start_price'], i['max_price'], i['min_price'], i['stop_price']])

c = (
    Kline(init_opts=opts.InitOpts(width="1440px", height="800px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        "kline",
        y_data,
        itemstyle_opts=opts.ItemStyleOpts(
            color="#ec0000",
            color0="#00da3c",
            border_color="#8A0000",
            border_color0="#008F28",
        ),
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True),
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        title_opts=opts.TitleOpts(title="abc003 K线走势图"),
    )
    .render("abc003kline.html")
)
