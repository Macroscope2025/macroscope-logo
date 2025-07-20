import os

def handler(request):
    with open("logo.png", "rb") as f:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/png"
            },
            "body": f.read().decode("latin1"),
            "isBase64Encoded": False
        }
