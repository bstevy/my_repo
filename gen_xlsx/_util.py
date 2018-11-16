import datetime
import calendar

today = datetime.datetime.today()
month = today.strftime("%Y-%m")
month_name = today.strftime("%Y%m")
start = datetime.datetime.strptime(month_name, '%Y%m')


day = {
    'Lu': 1,
    'Ma': 2,
    'Me': 3,
    'Je': 4,
    'Ve': 5,
}

date = {i: [] for i in range(1, 6, 1)}

for i in range(calendar.monthrange(today.year, today.month)[1]):
    d = start.isoweekday()
    if d in date:
        date[d].append(start.strftime("%Y-%m-%d"))
    start += datetime.timedelta(days=1)


def gen_out_line(cours_string):
    return ["autre", "", "", ] + date[day[cours_string[:2]]] + ["commentaire"]


def compteur():
    cnt = 0
    while True:
        yield cnt
        cnt += 1


def get_nb_jour(cours):
    return len(date[day[cours[:2]]])
