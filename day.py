import datetime

now = datetime.datetime.now()
weekdays = []

for i in range(0, -7, -1):
    now_before = str(now + datetime.timedelta(days=i))
    weekdays.append(now_before[:10])

print(weekdays)