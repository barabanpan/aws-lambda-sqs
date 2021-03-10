import json


def do_task(event, context):
    data = json.loads(event['Records'][0]['body'])
    print("NUM:", data.get("num"))

    # do task and return answer
