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
    """

    :param cours_string:
    :return:
    """
    return ["autre", "", "", ] + date[day[cours_string[:2]]] + ["commentaire"]


def compteur():
    """

    :return:
    """
    cnt = 0
    while True:
        yield cnt
        cnt += 1


def get_nb_jour(cours):
    """

    :param cours:
    :return:
    """
    return len(date[day[cours[:2]]])


def gen_footer(worksheet, cours, format_dict, compteur, max_line, footer_lines=8):
    """

    :param worksheet:
    :param cours:
    :param nb_jour:
    :param format_dict:
    :param compteur:
    :param max_line:
    :param footer_lines:
    :return:
    """
    nb_jour = get_nb_jour(cours)
    max_1, max_2 = max_line
    _ = next(compteur)
    _ = next(compteur)
    out_line = gen_out_line(cours)
    worksheet.write_row(next(compteur), 1, out_line, format_dict["bold_border"])
    for _ in range(footer_lines):
        worksheet.write_row(next(compteur), 1, list(" " * (4 + nb_jour)), format_dict["border"])
    index = next(compteur) + 1
    worksheet.merge_range(index, 1, index, 2, 'total présence', format_dict["merge_format"])
    worksheet.write_row(index, 4, list(" " * nb_jour), format_dict["bold_border"])
    worksheet.set_column(1, 1, int(max_1 * 1.25))
    worksheet.set_column(2, 2, int(max_2 * 1.25))
