import cv2 as cv

video = cv.VideoCapture()

ip = ""

video.open(ip)

while True:
    check, img = video.read()
    cv.imshow('Video', img)

    cv.waitKey(1)