import dropbox
import os

path = os.path.dirname(
    os.path.abspath(__file__)
)


def run(xlsx_path):
    """

    :return:
    """

    xlsx_name = os.path.basename(xlsx_path)
    dropbox_path = '/CDS-Laissez Nous Danser/4. Organisation annuelle/Suivi adhérents/2018-19/presence/{}'
    dropbox_path = dropbox_path.format(xlsx_name)

    with open(os.path.join(path, 'param')) as param:
        auth_token = param.readline()

    with open(xlsx_path, 'rb') as f:
        data = f.read()

    mode = dropbox.files.WriteMode.overwrite

    client = dropbox.Dropbox(auth_token)
    _ = client.files_upload(
        data,
        dropbox_path,
        mode,
        mute=True
    )

    os.remove(xlsx_path)
