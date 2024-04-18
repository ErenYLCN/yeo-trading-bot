import json


def pr(response):
    print(json.dumps(response, indent=4))


def p(response):
    return json.dumps(response, indent=4)
