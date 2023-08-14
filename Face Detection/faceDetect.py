from random import randrange
import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('group.jpg')

# Convert to grayscale
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)


for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 255), randrange(128, 255), randrange(128, 255)), 2)

# print(face_coordinates)

cv2.imshow("Face Detector Python", img)
cv2.waitKey()

print("Code Completed")
