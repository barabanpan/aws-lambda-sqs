import os
import boto3
import uuid

client = boto3.client("sqs")
sqs_url = os.getenv("SQS_URL")

def send(event, context):
    """Sends messages to SQS."""
    response = do_batch(event)
    #response = do_one_by_one(event)
    return response


def do_one_by_one(event):
    responses = []
    for i in range(5):
        message = {
            "num": str(i + 1)
        }
        responses.append(
            client.send_message(
                QueueUrl=sqs_url,
                MessageBody=json.dumps(message)
            )
        )
    return responses
    

def do_batch(event):
    entries = []
    for i in range(5):
        message = {
            "num": str(i + 1)
        }
        entries.append({
            'Id': str(uuid.uuid4()),
            'MessageBody': json.dumps(message)
        })

    response = client.send_message_batch(
        QueueUrl=sqs_url,
        Entries=entries
    )

