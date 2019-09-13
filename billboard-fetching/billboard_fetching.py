import billboard

from datetime import date, timedelta

def fetchchart(chartname, date=date.today()):
    print('fetching from %s at week of %s' % (chartname, date))

if __name__ == '__main__':
    interval = timedelta(days=7)
    currentweek = date(1963, 8, 17)
    chart = 'billboard-100'

    while currentweek < date.today(): 
        fetchchart(chart, currentweek)
        currentweek += interval 

