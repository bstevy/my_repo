import os

import get_csv
import gen_xlsx
import upload_dropbox

path = os.path.dirname(
    os.path.abspath(__file__)
)


def main():

    get_csv.run()
    xlsx_path = gen_xlsx.run(path)
    upload_dropbox.run(xlsx_path)
