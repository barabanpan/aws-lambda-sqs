import os
import boto3
import uuid
import json

client = boto3.client("sqs")
sqs_url = os.getenv("SQS_URL")

def send(event, context):
    """Sends messages to SQS."""
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

