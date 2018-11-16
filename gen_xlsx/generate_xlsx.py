import xlsxwriter
import os

from gen_xlsx._util import *


def run(path):

    last_cours = None

    c = compteur()

    xlsx_name = "presence_{date}.xlsx".format(date=month_name)
    xlsx_path = os.path.join(path, xlsx_name)

    with xlsxwriter.Workbook(xlsx_path) as workbook:

        bold_border = workbook.add_format({
            'bold': True,
            'border': True,
        })
        border = workbook.add_format({'border': True})
        bold = workbook.add_format({'bold': True})
        worksheet = None

        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'
        })

        line = {
            0: workbook.add_format({'border': True}),
            1: workbook.add_format({'border': True, 'fg_color': '#E0E0E0'}),
        }

        for l in open(os.path.join(path, "extract.csv"), encoding='utf8'):
            cours, role, firstname, lastname, abo = l.replace('"', '').strip().split(",")

            if cours != last_cours:
                if worksheet:
                    _ = next(c)
                    _ = next(c)
                    out_line = gen_out_line(cours)
                    worksheet.write_row(next(c), 1, out_line, bold_border)
                    for _ in range(3):
                        worksheet.write_row(next(c), 1, list(" " * (4 + nb_jour)), border)
                    index = next(c) + 1
                    worksheet.merge_range(index, 1, index, 2, 'total présence', merge_format)
                    worksheet.write_row(index, 4, list(" " * nb_jour), bold_border)
                    worksheet.set_column(1, 1, int(max_1 * 1.25))
                    worksheet.set_column(2, 2, int(max_2 * 1.25))

                last_role = ""
                if cours == "LuHH_2":
                    _ = next(c)
                    _ = next(c)
                    _ = next(c)
                else:
                    if cours == "LuHH_1":
                        worksheet = workbook.add_worksheet("LuHH_1_2")
                    else:
                        worksheet = workbook.add_worksheet(cours)
                    c = compteur()
                    max_1 = max_2 = 0
                worksheet.write(next(c), 1, cours, bold)
                worksheet.write(next(c), 1, month, bold)
                worksheet.set_column(0, 0, 1)
                worksheet.fit_to_pages(1, 1)
                nb_jour = get_nb_jour(cours)
                worksheet.set_column(4, 4 + nb_jour - 1, int(8 * 1.25))
                worksheet.set_column(4 + nb_jour, 4 + nb_jour, 30)
                worksheet.set_column(3, 3, 5)
                worksheet.set_margins(
                    left=0.25,
                    right=0.25,
                )

            if role != last_role:
                _ = next(c)
                _ = next(c)
                out_line = gen_out_line(cours)
                out_line[0] = role
                out_line[2] = "abo"
                worksheet.write_row(next(c), 1, out_line, bold_border)

            index = next(c)
            worksheet.write_row(index, 1, [firstname, lastname, abo, *(" " * (1 + nb_jour))], line[index % 2])
            max_1 = max(max_1, len(firstname))
            max_2 = max(max_2, len(lastname))
            last_cours = cours
            last_role = role

        _ = next(c)
        _ = next(c)
        out_line = gen_out_line(cours)
        worksheet.write_row(next(c), 1, out_line, bold_border)
        for _ in range(3):
            worksheet.write_row(next(c), 1, list(" " * (4 + nb_jour)), border)
        index = next(c) + 1
        worksheet.merge_range(index, 1, index, 2, 'total présence', merge_format)
        worksheet.write_row(index, 4, list(" " * nb_jour), bold_border)
        worksheet.set_column(1, 1, int(max_1 * 1.25))
        worksheet.set_column(2, 2, int(max_2 * 1.25))

    return xlsx_path
