import os
import base64

def handler(request):
    # Get the correct path to logo.png
    logo_path = os.path.join(os.path.dirname(__file__), "..", "logo.png")
    logo_path = os.path.abspath(logo_path)

    try:
        with open(logo_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "image/png"
                },
                "body": encoded,
                "isBase64Encoded": True
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error reading logo.png: {str(e)}"
        }
