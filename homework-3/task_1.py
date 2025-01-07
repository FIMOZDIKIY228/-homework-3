import datetime
from datetime import date
from datetime import datetime

today = datetime.today()
new_year_date = datetime(2026, 1, 1, 0,0)
print(new_year_date)
time_until_new_year = new_year_date - today
print(time_until_new_year)
print('До Нового года осталось дней:',time_until_new_year.days,',часов', time_until_new_year.seconds / 3600, ',минут', time_until_new_year.seconds / 60)