import requests
import infra.config_reader as config_reader


def send_post_message(path, massage):
    try:
        r = requests.post(url='http://' + config_reader.host + config_reader.port + path, json=massage)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def send_put_message(path, massage):
    try:
        r = requests.put(url='http://' + config_reader.host + config_reader.port + path, json=massage)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def send_get_message(path):
    try:
        r = requests.get(url='http://' + config_reader.host + config_reader.port + path)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def send_delete_message(path):
    try:
        r = requests.delete(url='http://' + config_reader.host + config_reader.port + path)
        return r
    except requests.exceptions.RequestException as e:
        print(e)

