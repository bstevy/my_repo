import os

import gen_xlsx
import upload_dropbox

path = os.path.dirname(
    os.path.abspath(__file__)
)

# path = os.path.abspath(os.curdir)


def main():

    xlsx_path = gen_xlsx.run(path)
    upload_dropbox.run(xlsx_path)


if __name__ == "__main__":

    main()
