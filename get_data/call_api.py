import requests
import os

path = os.path.dirname(
    os.path.abspath(__file__)
)


def get_data():
    """

    :return:
    """

    url = 'https://asso.laissez-nous-danser.com/__private_api/get_extract_record_attendance'

    with open(os.path.join(path, "param")) as in_file:
        key = in_file.read()

    params = {
        "gerak": key
    }

    resp = requests.get(url=url, params=params)
    data = resp.json()

    return data
