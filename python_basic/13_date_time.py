import datetime
import pytz

d = datetime.date(2018, 11, 11)
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)


print(d)  # 2018-11-11
print(tday)  # 2018-11-11
print(tday.year)  # 2018
print(tday.weekday())  # 6          Sunday = 6
print(tday.isoweekday())  # 7          Sunday = 7

print(tday - tdelta)  # 2018-11-04

bday = datetime.date(2019, 5, 30)
till_bday = bday - tday
print(till_bday)
print(till_bday.days)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45)

print(dt.date())
print(dt.time())
print(dt.year)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()            # can set timezone
dt_utcnow = datetime.datetime.utcnow()  # can set UTC

print(dt_today)
print(dt_now)
print(dt_utcnow)

# dt_utc = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utc)

# dt_tw = dt_utc.astimezone(pytz.timezone('Asia/Taipei'))
# print(dt_tw)

dt_jp = dt_now.astimezone(pytz.timezone('Asia/Tokyo'))
print(dt_jp)

print(datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo')))

print(dt_now.strftime('%B %d %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# for tz in pytz.all_timezones:
#     print(tz)
