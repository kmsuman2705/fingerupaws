#!/usr/bin/python3
import cgi
import os
import cv2
from cvzone.HandTrackingModule import HandDetector

# Print the content-type header
print("Content-Type: text/html")
print()

# HTML start
print("<html><body>")

# Upload directory
upload_dir = "/var/www/cgi-bin/myupload"

try:
    # Get the uploaded file
    form = cgi.FieldStorage()
    image_file = form['image']

    if image_file.filename:
        filename = "myimage.png"
        filepath = os.path.join(upload_dir, filename)

        # Save the uploaded image
        with open(filepath, 'wb') as f:
            f.write(image_file.file.read())
        print("<p>Image uploaded successfully.</p>")
    else:
        print("<p>No image file received</p>")
except Exception as e:
    print("<p>An error occurred:</p>", str(e))

# Initialize the hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Read the uploaded image
img = cv2.imread(filepath)

# Detect hands in the image
hands = detector.findHands(img, draw=False)
if hands:
    hand = hands[0]
    if hand:
        print("<h1>Hello Suman</h1>")
    else:
        print("<p>Multiple fingers up!</p>")
else:
    print("<p>No hand detected</p>")

# HTML end
print("</body></html>")
