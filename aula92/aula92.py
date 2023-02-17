# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta

data = datetime(2022, 10, 24, 15, 43, 20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strptime('24/10/2022', '%d/%m/%Y'))
timestamp = data.timestamp()

print(datetime.fromtimestamp(timestamp))

print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

somadata = data + timedelta(days=5, seconds=2*60*60)

print(somadata.strftime('%d/%m/%Y %H:%M:%S'))

print(50*'#')

d1 = data.strptime('01/01/2022 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = data.strptime('05/01/2022 22:33:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1
print(dif.seconds)
