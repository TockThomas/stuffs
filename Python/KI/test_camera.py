import cv2
import numpy as np

video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)
kernel = np.ones((5, 5), np.uint8)
faceCascade = cv2.CascadeClassifier("D:\Python\KI\haarcascades\haarcascade_frontalface_default.xml")

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty) #0
cv2.createTrackbar("Hue Max", "TrackBars", 80, 179, empty) #80
cv2.createTrackbar("Sat Min", "TrackBars", 100, 255, empty) #100
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty) #255
cv2.createTrackbar("Val Min", "TrackBars", 115, 255, empty) #115
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty) #255

h_min = cv2.getTrackbarPos("HueMin", "TrackBars")
print(h_min)

while True:
    success, img = video.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(img, 150, 200)
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
    imgResize = cv2.resize(img, (1280, 768))
    imgCropped = img[0:200, 200:500]
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    #print(img.shape)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    maskResult = cv2.bitwise_and(img, img, mask=mask)
    #faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Original", img)
    #cv2.imshow("Gray", imgGray)
    #cv2.imshow("Blur", imgBlur)
    #cv2.imshow("Canny", imgCanny)
    #cv2.imshow("Dialation", imgDialation)
    #cv2.imshow("Eroded", imgEroded)
    #cv2.imshow("Rezise", imgResize)
    #cv2.imshow("Rezise", imgCropped)
    #cv2.imshow("HSV", imgHSV)
    #cv2.imshow("Mask", mask)
    cv2.imshow("Mask-Result", maskResult)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break