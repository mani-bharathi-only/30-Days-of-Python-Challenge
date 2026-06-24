from datetime import datetime
now=datetime.now()
day=now.day
month=now.month
year=now.year
hour=now.hour
timestammp=now.timestamp()
print("timestamp",timestammp)
print(f"{day}/{month}/{year}")