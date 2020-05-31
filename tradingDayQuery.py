import urllib.request as request
import datetime

'''
@query a single date: string '20170401';
@api return day_type: 0 workday 1 weekend 2 holiday -1 err
@function return day_type: 1 workday 0 weekend&holiday
'''


def get_day_type(query_date):
    url = 'http://tool.bitefu.net/jiari/?d=' + query_date
    resp = request.urlopen(url)
    content = resp.read()
    if content:
        try:
            day_type = int(content)
        except ValueError:
            return -1
        else:
            return day_type
    else:
        return -1


def is_tradeday(query_date):
    weekday = datetime.datetime.strptime(query_date, '%Y-%m-%d').isoweekday()
    if weekday <= 5 and get_day_type(query_date) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    query_date = datetime.datetime.strftime(datetime.datetime.today(), '%Y-%m-%d')
    print(query_date)
    print(is_tradeday(query_date))