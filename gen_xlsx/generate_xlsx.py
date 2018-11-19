import xlsxwriter
import os

from get_data import get_data
from gen_xlsx._util import *


def run(path):

    last_cours = None

    c = compteur()

    xlsx_name = "presence_{date}.xlsx".format(date=month_name)
    xlsx_path = os.path.join(path, xlsx_name)

    with xlsxwriter.Workbook(xlsx_path, {'constant_memory': True}) as workbook:

        format_dict = dict()

        format_dict["bold_border"] = workbook.add_format({
            'bold': True,
            'border': True,
        })
        format_dict["border"] = workbook.add_format({'border': True})
        format_dict["bold"] = workbook.add_format({'bold': True})
        worksheet = None

        format_dict["merge_format"] = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'
        })

        format_dict["line"] = {
            0: workbook.add_format({'border': True}),
            1: workbook.add_format({'border': True, 'fg_color': '#E0E0E0'}),
        }

        for line in get_data():
            cours = line["niveau"]
            role = line["role"]
            firstname = line["firstname"]
            lastname = line["lastname"]
            abo = line["abo"]

            if cours != last_cours:
                if worksheet:
                    gen_footer(worksheet, last_cours, format_dict, c, (max_1, max_2))

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
                worksheet.write(next(c), 1, cours, format_dict["bold"])
                worksheet.write(next(c), 1, month, format_dict["bold"])
                worksheet.set_column(0, 0, 1)
                worksheet.fit_to_pages(1, 1)
                nb_jour = get_nb_jour(cours)
                worksheet.set_column(4, 4 + nb_jour - 1, int(8 * 1.25))
                worksheet.set_column(4 + nb_jour, 4 + nb_jour, 30)
                worksheet.set_column(3, 3, 5)
                worksheet.set_margins(
                    left=0.25,
                    right=0.25,
                    top=0.25,
                    bottom=0.25,
                )

            if role != last_role:
                _ = next(c)
                _ = next(c)
                out_line = gen_out_line(cours)
                out_line[0] = role
                out_line[2] = "abo"
                worksheet.write_row(next(c), 1, out_line, format_dict["bold_border"])

            index = next(c)
            worksheet.write_row(
                index, 1,
                [firstname, lastname, abo, *(" " * (1 + nb_jour))],
                format_dict["line"][index % 2]
            )
            max_1 = max(max_1, len(firstname))
            max_2 = max(max_2, len(lastname))
            last_cours = cours
            last_role = role

        gen_footer(worksheet, cours, format_dict, c, (max_1, max_2))

    return xlsx_path
