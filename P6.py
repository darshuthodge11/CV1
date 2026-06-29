import cv2

# Load the pre-trained pedestrian detector
pedestrian_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Load the input image
image = cv2.imread("C:/Users/Darshana/OneDrive/Desktop/MSCIT SEM 2/MSC IT SEM 2 COMPUTER VISION/pedestrainimg.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect pedestrians in the image
pedestrians = pedestrian_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(5, 5))

# Draw rectangles around the detected pedestrians
for (x, y, w, h) in pedestrians:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with pedestrian detections
cv2.imshow('Pedestrian Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

