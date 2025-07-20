import datetime
from flask import Response
import base64

def handler(request):
    now = datetime.datetime.now()

    # Adjust for UK time (UTC+1 during BST)
    uk_hour = (now.hour + 1) % 24

    # Choose logo based on time
    if uk_hour < 17:  # Before 5 PM UK time
        logo_path = "Macroscope-burgundy-logo.png"
    else:
        logo_path = "Macroscope-green-logo.png"

    # Load and return the image
    with open(logo_path, "rb") as f:
        image_data = f.read()

    return Response(
        image_data,
        content_type="image/png"
    )
