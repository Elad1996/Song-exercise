import json

status_templates = {
    "p_ok": r"2\d{2}",

    "p_fail": r"4\d{2}"
}


def response(r):
    if 'error' in r.text:
        body_dict = json.loads(r.text)
        return body_dict['error']

    if 'message' in r.text:
        body_dict = json.loads(r.text)
        if body_dict['message'] == 'OK':
            return body_dict['data']

    return False
